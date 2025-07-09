import logging
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
import sys

# Set up logging
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        logging.info("Bot initialized (Testnet mode: %s)", testnet)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                "symbol": symbol.upper(),
                "side": SIDE_BUY if side.lower() == "buy" else SIDE_SELL,
                "type": order_type,
                "quantity": quantity,
            }

            if order_type == ORDER_TYPE_LIMIT:
                params["price"] = price
                params["timeInForce"] = TIME_IN_FORCE_GTC

            response = self.client.futures_create_order(**params)
            logging.info("Order placed: %s", response)
            print("Order executed:", response['orderId'])
        except BinanceAPIException as e:
            logging.error("API Error: %s", e)
            print("API Error:", e.message)
        except Exception as e:
            logging.error("Unexpected Error: %s", e)
            print("---Error:", str(e))

