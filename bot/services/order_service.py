from bot.client.binance_client import BinanceFuturesClient
from bot.validators.order_validator import validate_order_input
from bot.logging.logger import get_logger

logger = get_logger("OrderService")


class OrderService:
    def __init__(self):
        self.client = BinanceFuturesClient()

    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: float | None = None,
    ) -> dict:

        validate_order_input(symbol, side, order_type, quantity, price)

        order_params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            order_params.update(
                {
                    "price": price,
                    "timeInForce": "GTC",
                }
            )

        logger.info(f"Placing {order_type} order for {symbol}")
        return self.client.create_order(order_params)
