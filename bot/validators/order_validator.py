from bot.exceptions import ValidationError
from bot.config.settings import SUPPORTED_ORDER_TYPES, SUPPORTED_SIDES


def validate_order_input(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float | None,
):
    if not symbol or not symbol.isalnum():
        raise ValidationError("Invalid or empty trading symbol")

    if side not in SUPPORTED_SIDES:
        raise ValidationError("Side must be BUY or SELL")

    if order_type not in SUPPORTED_ORDER_TYPES:
        raise ValidationError("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValidationError("Quantity must be greater than 0")

    if order_type == "LIMIT":
        if price is None or price <= 0:
            raise ValidationError("Price must be provided and > 0 for LIMIT orders")
