class Car:
    def __init__(self, brand: str, max_speed: int, mileage: int):
        self.brand = brand
        self.max_speed = max_speed
        self.mileage = mileage
    
    def show_info(self):
        print((f"Car brand: {self.brand}, Maximum speed: {self.max_speed}, Mileage: {self.mileage}."))

Ferrari = Car("Ferrari", 205, 21)
Ferrari.show_info()

###
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
        # super().__init__ is often used in single-inheritance scenarios where there is only one parent class. It simplifies the code by letting Python determine the appropriate parent class automatically.

class Lamborghini(Car):
    def __init__(self, max_speed: int, mileage: int):
        super().__init__(brand="Lamborghini", max_speed=max_speed, mileage=mileage)

Car1 = Ferrari(205, 21)
Car1.show_info()

Car2 = Lamborghini(200, 15)
Car2.show_info()

# Bioinformatics senarior: create a parent class called SequenceAnalyzer and two child classes, DNAAnalyzer and RNAAnalyzer, to analyze the base distribution of DNA and RNA sequences. 
class SequenceAnalyzer:
    def __init__(self, sequence: str):
        self.sequence = sequence
    def analyze(self):
        raise NotImplementedError("Subclasses must implement the analyze method.")
    def show_info(self):
        pass

class DNAAnalyzer(SequenceAnalyzer):
    def analyze(self):
        base_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        total_bases = len(self.sequence)
        for base in self.sequence:
            if base in base_counts:
                base_counts[base] += 1
        gc_content = (base_counts['G'] + base_counts['C']) / total_bases * 100
        self.analysis_results = {
            "Sequence": self.sequence,
            "Total bases": total_bases,
            "A Count": base_counts['A'],
            "T Count": base_counts['T'],
            "C Count": base_counts['C'],
            "G Count": base_counts['G'],
            "GC Content": f"{gc_content:.2f}%"
        }
    def show_info(self):
        print("Analyzing DNA sequence:")
        for key, value in self.analysis_results.items():
            print(f"{key}: {value}")

class RNAAnalyzer(SequenceAnalyzer):
    def analyze(self):
        base_counts = {'A': 0, 'U': 0, 'C': 0, 'G': 0}
        total_bases = len(self.sequence)
        for base in self.sequence:
            if base in base_counts:
                base_counts[base] += 1
        gc_content = (base_counts['G'] + base_counts['C']) / total_bases * 100
        self.analysis_results = {
            "Sequence": self.sequence,
            "Total bases": total_bases,
            "A Count": base_counts['A'],
            "U Count": base_counts['U'],
            "C Count": base_counts['C'],
            "G Count": base_counts['G'],
            "GC Content": f"{gc_content:.2f}%"
        }
    def show_info(self):
        print("Analyzing RNA sequence:")
        for key, value in self.analysis_results.items():
            print(f"{key}: {value}")

# Example usage:
dna_sequence = "ATCGATCGTTCG"
rna_sequence = "AUCUAUCGAUCG"

dna_analyzer = DNAAnalyzer(dna_sequence)
rna_analyzer = RNAAnalyzer(rna_sequence)

dna_analyzer.analyze()
rna_analyzer.analyze()

dna_analyzer.show_info()
rna_analyzer.show_info()
