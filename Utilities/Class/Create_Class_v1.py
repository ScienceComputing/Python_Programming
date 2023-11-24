# Add methods/functions to a class
class RNASample:
    def __init__(self):
        self.name = None
        self.expression_values = []
    def set_name(self, new_name):
        self.name = new_name
    def set_expression_values(self, values):
        self.expression_values = values
    def calculate_mean_expression(self):
        if not self.expression_values:
            return 0
        return sum(self.expression_values) / len(self.expression_values)
    def calculate_max_expression(self):
        if not self.expression_values:
            return 0
        return max(self.expression_values)

rna_sample = RNASample()
rna_sample.set_name('Sample_001')
expression_values = [10.1, 16.3, 2.1, 1.1, 10.8]
rna_sample.set_expression_values(expression_values)

mean_expression = rna_sample.calculate_mean_expression()
print(f"Mean Expression: {mean_expression}")

max_expression = rna_sample.calculate_max_expression()
print(f"Max Expression: {max_expression}")


class Falafel:
    def __init__(self,type='baked'): # use self as the 1st argument in method definition; self refers to the data of a particualr object
        self.ingrediate = ['Chickpeas', 'Onion', 'Parsley', 'Garlic', 'Green Chile Pepper', 'Oil', 'Baking Soda'] # Create the attribute ingrediate
        self.type = type
        if self.type not in ['fried','baked']:
            print('Unrecognized type: ' + str(self.type))
            print('Type will be set to baked')
            self.type = 'baked'
        self.origin = 'Egyptian cuisine'
    def eat(self):
        print('I got eaten')
    def new_origin(self):
        self.origin = 'Levantine cuisine'
        print('I bought' + self.origin)

class MultiFalafel(Falafel): 
    def __init__(self,num=1,num_to_eat=1):
        self.number = num
        self.number_eat = num_to_eat
        if self.number_eat > self.number:
            print('Reset the number of falafels eaten '+str(num_to_eat)+' to the total number of falafels '+str(num))
            self.number_eat = num
        Falafel.__init__(self)
        print(str(num)+' falafel(s) created')
    def eat(self):
        print(str(self.number_eat)+' falafel(s) got eaten')
        self.remaining = self.number - self.number_eat

# Test the code
# six_falafels = MultiFalafel(num=6,num_to_eat=7) # Ignore self when calling method on an object
# six_falafels.eat()
# six_falafels.remaining
# six_falafels.type
# six_falafels.ingrediate
# six_falafels.new_origin()
