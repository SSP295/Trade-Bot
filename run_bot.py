from trading_bot import BasicBot

def main():
    api_key = input("Enter your API key: ").strip()
    api_secret = input("Enter your API secret: ").strip()

    bot = BasicBot(api_key, api_secret)

    symbol = input("Enter trading symbol (e.g., BTCUSDT): ")
    side = input("Order side (buy/sell): ").lower()
    order_type = input("Order type (MARKET/LIMIT): ").upper()
    quantity = float(input("Quantity: "))
    price = None

    if order_type == "LIMIT":
        price = input("Enter limit price: ")

    bot.place_order(symbol, side, order_type, quantity, price)

if __name__ == "__main__":
    main()
