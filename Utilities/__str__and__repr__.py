class Stock:
    def __init__(self, symbol: str, price: float, quantity: int):
        """Initialize a Stock object with a symbol, price per share, and quantity of shares."""
        self.symbol = symbol
        self.price = price
        self.quantity = quantity
    def buy(self, amount: float):
        """Buy a specified dollar amount of shares and update the quantity of shares."""
        self.quantity += amount / self.price
    def sell(self, amount: float):
        """Sell a specified dollar amount of shares if enough shares are available."""
        if self.quantity >= amount / self.price:
            self.quantity -= amount / self.price
            return True
        else:
            return False
    def __str__(self):
        """Return a string representation of the Stock object."""
        return f"{self.symbol}: {self.quantity} shares at ${self.price} per share"
    def __repr__(self):
        """Return a string representation for creating a new Stock object."""
        return f"Stock({self.symbol}, {self.price}, {self.quantity})"


# Example usage with Google's stock
google_stock = Stock("GOOG (NASDAQ)", 135.37, 20)
print(google_stock) # This will call the __str__ method 

# Buy more shares
google_stock.buy(5000)
print(google_stock) # This will call the __repr__ method 

# Sell some shares
if google_stock.sell(10000):
    print(f"Sold 10000 dollars worth of {google_stock.symbol} shares successfully.")
else:
    print(f"Not enough shares to sell 10000 dollars worth of {google_stock.symbol} shares.")
