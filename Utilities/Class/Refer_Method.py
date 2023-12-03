class Car:
    def __init__(self, make, model):
        self.make, self.model = make, model
    def start_engine(self):
        self.print_message("Engine started.")
    def accelerate(self):
        self.print_message("Car is accelerating.")
    def print_message(self, message):
        print(message)

my_car = Car(make="Toyota", model="Camry")

my_car.start_engine() # Engine started.
my_car.accelerate() # Car is accelerating.
