# Create a class with attributes
class Car1:
    max_speed = 300
    mileage = 20

# Create a class with instance attributes
class Car2:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

m1 = Car1()
m2 = Car2(300, 20)

m1.max_speed
# 300
m2.max_speed
# 300

# Create a class with no attributes and methods
class Car3:
    pass

# Create a child class Tesla that will inherit all of the attributes and methods of the car class
class Car:
    def __init__(self, brand, max_speed, mileage):
        self.brand = brand
        self.max_speed = max_speed
        self.mileage = mileage

class Tesla(Car):
    pass
m4 = Tesla("Tesla", 360, 30)
print ("Car brand: {}, Maximum speed: {}, Mileage: {}.".format(m4.brand, m4.max_speed, m4.mileage))
