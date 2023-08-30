class Car:
    def __init__(self, brand: str, max_speed: int, mileage: int):
        self.brand = brand
        self.max_speed = max_speed
        self.mileage = mileage
    
    def show_info(self):
        print((f"Car brand: {self.brand}, Maximum speed: {self.max_speed}, Mileage: {self.max_speed}."))

Ferrari = Car("Ferrari", 205, 21)
Ferrari.show_info()
