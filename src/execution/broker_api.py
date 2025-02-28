import alpaca_trade_api as tradeapi

API_KEY = "AK4IFAHP4JTVN05N18XQ"
API_SECRET = "ONvGmTvEFEseNdwB8PF7EKr9dusVCwifMNXmH00R"
BASE_URL = "https://paper-api.alpaca.markets"  # Use paper trading for testing

alpaca = tradeapi.REST(API_KEY, API_SECRET, BASE_URL)

def place_order(symbol, qty, side):
    try:
        alpaca.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type="market",
            time_in_force="gtc"
        )
        print(f"Order placed: {side} {qty} of {symbol}")
    except Exception as e:
        print(f"Error placing order: {e}")
