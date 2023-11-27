import pandas as pd

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def record(self):
        return f"{self.year} {self.make} {self.model}"

class DataAnalyzer:
    def __init__(self, car_data):
        self.car_data = car_data
    def analyze(self):
        print("Analyzing car data:")
        for car in self.car_data:
            description = car.record()
            print(description)
    @classmethod # Build a class-level method, such that we can call this method directly from the class DataAnalyzer, instead of an object
    def from_csv(cls, csv_path):
        # Use Pandas to read data from the CSV file
        df = pd.read_csv(csv_path)
        # Extract data from the DataFrame and create Car objects
        car_data = []
        for index, row in df.iterrows():
            make = row['Make']
            model = row['Model']
            year = row['Year']
            car = Car(make, model, year)
            car_data.append(car)
        return cls(car_data)
    @classmethod
    def from_dataframe(cls, df):
        car_data = []
        for index, row in df.iterrows():
            make = row['Make']
            model = row['Model']
            year = row['Year']
            car = Car(make, model, year)
            car_data.append(car)
        return cls(car_data)

# Example usage:
# Assume we have a CSV file named "car_data.csv" with columns "Make", "Year", and "Model"
analyzer_1 = DataAnalyzer.from_csv("Desktop/car_data.csv") #! Class-level method
analyzer_1.analyze()

# Assume we have a pandas data frame names "car_data" at hand with columns "Make", "Model", and "Year"
car_data = pd.DataFrame({
    'Make': ['Toyota', 'Honda', 'Ford'],
    'Model': ['Camry', 'Civic', 'Fusion'],
    'Year': ['2022', '2021', '2020']
})
analyzer_2 = DataAnalyzer.from_dataframe(car_data)
analyzer_2.analyze()
