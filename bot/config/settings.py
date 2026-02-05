import os
from dotenv import load_dotenv

load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

BINANCE_FUTURES_TESTNET_URL = "https://testnet.binancefuture.com"

LOG_FILE_PATH = "logs/trading_bot.log"

SUPPORTED_ORDER_TYPES = ["MARKET", "LIMIT"]
SUPPORTED_SIDES = ["BUY", "SELL"]
