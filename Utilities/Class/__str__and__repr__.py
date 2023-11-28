# The methods __str__ and __repr__ will return a printable representation (rather than the object's address in memory) of an object associated with a class.
# The recommended approach is to utilize 'repr' to display a string that can be used to recreate the object.

class Stock:
    def __init__(self, symbol: str, price: float, quantity: int):
        """
        Initialize a Stock object with a symbol, price per share, and quantity of shares.
        """
        self.symbol, self.price, self.quantity = symbol, price, quantity
    def buy(self, amount: float):
        """
        Buy a specified dollar amount of shares and update the quantity of shares.
        """
        self.quantity += amount / self.price
    def sell(self, amount: float):
        """
        Sell a specified dollar amount of shares if enough shares are available.
        """
        if self.quantity >= amount / self.price:
            self.quantity -= amount / self.price
            return True
        else:
            return False
    def __str__(self):
        """
        Return a string representation of the Stock object.
        """
        return f"{self.symbol}: {self.quantity} shares at ${self.price} per share"
    def __repr__(self):
        """
        Return a string representation for creating a new Stock object.
        """
        return f"Stock({self.symbol}, {self.price}, {self.quantity})"


# Example usage with Google's stock
google_stock = Stock("GOOG (NASDAQ)", 138.05, 20)
print(google_stock) # This will call the __str__ method 

# Buy more shares
google_stock.buy(5000)
print(repr(google_stock)) # This will call the __repr__ method 

# Sell some shares
if google_stock.sell(10000):
    print(f"Sold 10000 dollars worth of {google_stock.symbol} shares successfully.")
else:
    print(f"Not enough shares to sell 10000 dollars worth of {google_stock.symbol} shares.")
