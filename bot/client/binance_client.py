from binance.client import Client
from bot.config.settings import (
    BINANCE_API_KEY,
    BINANCE_API_SECRET,
    BINANCE_FUTURES_TESTNET_URL,
)
from bot.logging.logger import get_logger
from bot.exceptions import BinanceClientError

logger = get_logger("BinanceClient")


class BinanceFuturesClient:
    def __init__(self):
        try:
            self.client = Client(
                api_key=BINANCE_API_KEY,
                api_secret=BINANCE_API_SECRET,
                testnet=True,
            )
            self.client.FUTURES_URL = BINANCE_FUTURES_TESTNET_URL
            logger.info("Binance Futures Testnet client initialized")
        except Exception as exc:
            logger.error("Failed to initialize Binance client", exc_info=True)
            raise BinanceClientError(str(exc))

    def create_order(self, order_params: dict) -> dict:
        try:
            logger.info(f"Order Request: {order_params}")
            response = self.client.futures_create_order(**order_params)
            logger.info(f"Order Response: {response}")
            return response
        except Exception as exc:
            logger.error("Binance API error", exc_info=True)
            raise BinanceClientError(str(exc))
