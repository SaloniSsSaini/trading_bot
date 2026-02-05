## Note on API Authentication

Binance Futures Testnet currently enforces Ed25519-based API authentication.
The python-binance library requires HMAC (API key + secret) authentication for private endpoints.
Due to this authentication incompatibility, order execution fails after request initiation.
This limitation does not affect the application structure, CLI, validation, or logging.
