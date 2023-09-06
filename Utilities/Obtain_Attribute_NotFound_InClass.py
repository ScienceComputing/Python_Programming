class Car:
    def __init__(self, brand: str, max_speed: int, mileage: int):
        self.brand = brand
        self.max_speed = max_speed
        self.mileage = mileage
    def show_info(self):
        print((f"Car brand: {self.brand}, Maximum speed: {self.max_speed}, Mileage: {self.mileage}."))

Car1 = Car("Ferrari", 205, 21)

print("The brand of Car1 is", getattr(Car1, "brand", "Tesla"))

print("The price of Car1 is", getattr(Car1, "price", "inestimable"))
