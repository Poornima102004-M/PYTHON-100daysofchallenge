import random

class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

    def update_price(self):
        # Simulating price fluctuations
        change = random.uniform(-1, 1)
        self.price += change

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, stock, quantity):
        if stock.symbol in self.stocks:
            self.stocks[stock.symbol] += quantity
        else:
            self.stocks[stock.symbol] = quantity

    def remove_stock(self, stock, quantity):
        if stock.symbol in self.stocks:
            self.stocks[stock.symbol] -= quantity
            if self.stocks[stock.symbol] <= 0:
                del self.stocks[stock.symbol]

    def calculate_value(self):
        value = 0
        for symbol, quantity in self.stocks.items():
            if symbol in stock_market:
                value += stock_market[symbol].price * quantity
        return value

# Simulate a stock market with some initial stocks
stock_market = {'AAPL': Stock('AAPL', 150.0), 'GOOG': Stock('GOOG', 2500.0)}

# Create a portfolio for a user
portfolio = Portfolio()
portfolio.add_stock(stock_market['AAPL'], 10)
portfolio.add_stock(stock_market['GOOG'], 5)

# Simulate trading for some time
for _ in range(100):
    for symbol, stock in stock_market.items():
        stock.update_price()

# Check portfolio value after trading
print("Portfolio Value:", portfolio.calculate_value())
