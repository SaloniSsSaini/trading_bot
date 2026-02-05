class TradingBotError(Exception):
    """Base exception for trading bot"""


class ValidationError(TradingBotError):
    """Raised when user input validation fails"""


class BinanceClientError(TradingBotError):
    """Raised when Binance API interaction fails"""
