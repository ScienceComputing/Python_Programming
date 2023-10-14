# Why use the dataclasses?
# We can set default values for particular fields to ensure that each time we use a dataclass those fields are preset. 
# Dataclasses also provide a default representation for print, log and other outputs. 
# If we need to convert our dataclass to a dictionary or a tuple, dataclasses have functions that can perform that conversion for us.
# We can also make custom properties that do more than just store a value. 
# It's also possible to make frozen instances of a dataclass that doesn't allow any edits to the properties after the dataclass has been created.

from dataclasses import dataclass # Import dataclass from the dataclasses module
@dataclass
class Amino_acid:
    name: str
    function: str = None

First_aa = Amino_acid('Cysteine', 'Help prevent side effects due to drug reactions and toxic chemicals')
print(First_aa.name)
# Cysteine
print(First_aa.function)
# Help prevent side effects due to drug reactions and toxic chemicals


from dataclasses import asdict, astuple
First_aa = Amino_acid('Cysteine', 'Help prevent side effects due to drug reactions and toxic chemicals')
First_aa_dict = asdict(First_aa)
print(First_aa_dict)
# {'name': 'Cysteine', 'function': 'Help prevent side effects due to drug reactions and toxic chemicals'}
First_aa_tuple = astuple(First_aa)
print(First_aa_tuple)
# ('Cysteine', 'Help prevent side effects due to drug reactions and toxic chemicals')


from dataclasses import dataclass
from decimal import Decimal
@dataclass
class Price_entry:
    # Define the fields on the class
    food: str
    quantity: int
    unit_price: Decimal
        
    # Define a property that returns the total_price
    @property
    def Total_price(self):
        return int(self.quantity) * self.unit_price

Grazed_donut = Price_entry('Grazed_donut', 3, Decimal('2.5'))
Grazed_donut.Total_price
# Decimal('7.5')
