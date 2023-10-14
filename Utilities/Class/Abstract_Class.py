# Create different child classes to use the same attributes and methods of the parent class. But the implementation of those methods should be different in each child class.
class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year
    def start_engine(self):
        pass
    def stop_engine(self):
        pass

class ElectricCar(Car):
    def start_engine(self):
        print(f'{self.year} {self.make} {self.model} electric car is starting.')
    def stop_engine(self):
        print(f'{self.year} {self.make} {self.model} electric car is stopping.')

class GasolineCar(Car):
    def start_engine(self):
        print(f'{self.year} {self.make} {self.model} gasoline car is starting.')
    def stop_engine(self):
        print(f'{self.year} {self.make} {self.model} gasoline car is stopping.')

# Create instances of ElectricCar and GasolineCar
electric_car = ElectricCar("Tesla", "Model S", 2023)
gasoline_car = GasolineCar("Ford", "Mustang", 2023)

# Start and stop the engines
electric_car.start_engine()
electric_car.stop_engine()

gasoline_car.start_engine()
gasoline_car.stop_engine()

# Bioinformatics scenarior: create a hierarchy of classes to represent different types of single-cell data and analyses
class SingleCellData:
    def __init__(self, sample_id: str):
        self.sample_id = sample_id
    def preprocess(self):
        pass
    def analyze(self):
        pass

class RNASeqData(SingleCellData):
    def preprocess(self):
        print(f'Preprocessing RNA-seq data for sample {self.sample_id}')
    def analyze(self):
        print(f'Analyzing RNA-seq data for sample {self.sample_id}')

class ATACSeqData(SingleCellData):
    def preprocess(self):
        print(f'Preprocessing ATAC-seq data for sample {self.sample_id}')
    def analyze(self):
        print(f'Analyzing ATAC-seq data for sample {self.sample_id}')

# Create instances of RNASeqData and ATACSeqData
rna_seq_sample = RNASeqData("SC001")
atac_seq_sample = ATACSeqData("SC002")

# Preprocess and analyze the data
rna_seq_sample.preprocess()
rna_seq_sample.analyze()

atac_seq_sample.preprocess()
atac_seq_sample.analyze()
