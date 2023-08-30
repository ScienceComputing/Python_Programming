class Car:
    def __init__(self, brand: str, max_speed: int, mileage: int):
        self.brand = brand
        self.max_speed = max_speed
        self.mileage = mileage
    
    def show_info(self):
        print((f"Car brand: {self.brand}, Maximum speed: {self.max_speed}, Mileage: {self.mileage}."))

Ferrari = Car("Ferrari", 205, 21)
Ferrari.show_info()

class Car:
    def __init__(self, brand: str, max_speed: int, mileage: int):
        self.brand = brand
        self.max_speed = max_speed
        self.mileage = mileage
    
    def show_info(self):
        print((f"Car brand: {self.brand}, Maximum speed: {self.max_speed}, Mileage: {self.mileage}."))

class Ferrari(Car):
    def __init__(self, max_speed: int, mileage: int):
        super().__init__(brand="Ferrari", max_speed=max_speed, mileage=mileage)

class Lamborghini(Car):
    def __init__(self, max_speed: int, mileage: int):
        super().__init__(brand="Lamborghini", max_speed=max_speed, mileage=mileage)

Car1 = Ferrari(205, 21)
Car1.show_info()

Car2 = Lamborghini(200, 15)
Car2.show_info()
