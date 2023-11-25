A programming language can be either object-oriented or procedural, or both

## Procedural programming
- We treat codes asn a sequence of steps
- It is suitable for data analysis and scripts
- Procedural programming encourages us to inquire: what is the purpose of this program?

## Object-oriented programming (OOP)
- We treat codes as interactions of objects
- It is suitable for building frameworks and tools (e.g., application program interfaces, graphical user interfaces, pandas DataFrames)
- Better organize our codes, making them more resuable and maintainable
- OOP encourages us to inquire: what kind of environment does this program construct? what entities exist within it? how do they collaborate?

## Object
```
object = attributes/variables + methods/functions
```
- **Encapsulation** is a distinctive feature of OOP, which bundles the attributes with the methods operating on them
- The object is a realization of a class with particular attribute values
- In python, everything is an object, even a function is an object

```
# List all the attributes and methods of an object
dir(obj)
```

## Class
- It is an abstract template for objects, describing possible attributs and methods
- In python, everything has a class
```
# Find the class of an object
type(obj)

# Show the documentation of a class associated with an object
help(obj)
```

- Best practices
  - Use `__init__()` to define all attributes in one place
  - Use `CamelCase` to define the name of a class, use `lower_snake_case` to define functions and attributes
  - Keep `self` as `self`
  - Use docstrings to show the function of a class

## Instance-level data
```
class IntronicVariant:
    def __init__(self, gene, location, description):
        self.gene = gene
        self.location = location
        self.description = description

variant_1 = IntronicVariant('Gene_XYZ', 'Intron 3', 'A common intronic variant associated with disease M')
variant_1.gene # Instance-level attribute

```

## Class-level data
```
class IntronicVariant:
    min_intron_length = 20 # Define a class-level attribute, which is shared among all instances
    def __init__(self, gene, location, description, intron_length):
        self.gene = gene
        self.location = location
        self.description = description
        if intron_length >= IntronicVariant.min_intron_length:
            self.intron_length = intron_length
        else:
            self.intron_length = IntronicVariant.min_intron_length # Use ClassName.attrite_name to access the class-level attribute value

variant_1 = IntronicVariant('Gene_XYZ', 'Intron 3', 'A common intronic variant associated with disease M', 10)
variant_1.min_intron_length # 20
variant_1.intron_length # 20
```

## Class-level attributes
By using the class attributes, we can set up the global constants related to the class, for example, min and max values for attributes or commonly used values (e.g., $\pi$, Euler's number, Planck's constant).

## Class-level methods
- While it is feasible to define methods associated with a class rather than an instance, their practical use is limited since these methods cannot access any instance-level data.
- Its main usage is to provide an alternative constructor. A class can only have one `__init__` method, but there could be more than one way to initialize an object. 
```
class MyClass:
    class_variable = 0  # Class-level variable
    def __init__(self, value):
        self.value = value  # Instance-level variable
    def instance_method(self):
        print(f"Instance method called with value: {self.value}")
    @classmethod
    def class_method(cls): # Notice cls, not self; cls refers to a class
        cls.class_variable += 1
        print(f"Class method called. Class variable is now: {cls.class_variable}")

# Create instances of MyClass
obj1 = MyClass(1)
obj2 = MyClass(2)

# Call instance methods
obj1.instance_method() # Instance method called with value: 1
obj2.instance_method()

# Call class method
MyClass.class_method()
MyClass.class_method()
MyClass.class_method() # Class method called. Class variable is now: 3
```

```
# https://www.ncbi.nlm.nih.gov/clinvar/variation/37654/
class Gene:
    DEFAULT_INTRONIC_VARIANT = "no-variant"
    def __init__(self, name, intronic_variant=DEFAULT_INTRONIC_VARIANT):
        self.name = name
        self.intronic_variant = intronic_variant
    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as f:
            data = f.readline().strip().split(':')
            name = data[0]
            intronic_variant = data[1] if len(data) > 1 else cls.DEFAULT_INTRONIC_VARIANT
        return cls(name, intronic_variant)

gene = Gene.from_file("ClinVar_data.txt")
print(gene.name) # Output: BRCA1
print(gene.intronic_variant) # Output: c.5277+1G>A
```
