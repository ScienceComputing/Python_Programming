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


# Bioinformatics scenarior: create a class to represent individual samples from integrative single-cell RNA sequencing data 
# and obtain attributes that are not defined in this class
class SingleCellSample:
    def __init__(self, sample_name: str, cell_type: str, gene_expression: dict, metadata: dict):
        self.sample_name = sample_name
        self.cell_type = cell_type
        self.gene_expression = gene_expression
        self.metadata = metadata
    def show_info(self):
        print(f"Sample Name: {self.sample_name}")
        print(f"Cell Type: {self.cell_type}")
        print("Gene Expression:")
        for gene, expression in self.gene_expression.items():
            print(f"  {gene}: {expression}")
        print("Metadata:")
        for key, value in self.metadata.items():
            print(f"  {key}: {value}")

# Example usage
sample1_metadata = {"Age": 35, "Gender": "Female", "Treatment": "Control"}
sample1 = SingleCellSample("SSG_A", "Neuron", {"GAD1": 12.3, "SYT1": 9.8, "MAPT": 5.4}, sample1_metadata)

sample2_metadata = {"Age": 28, "Gender": "Male", "Treatment": "Experimental"}
sample2 = SingleCellSample("SSG_B", "T-cell", {"CD3E": 8.2, "CD4": 5.6, "CD8A": 7.1}, sample2_metadata)

# Access metadata attributes that are not defined in a class
print("Sample 1 cardiovascular history:", getattr(sample1, "metadata['CVD']", "Yes"))
print("Sample 2 cardiovascular history:", getattr(sample2, "metadata['CVD']", "CVD not available"))
