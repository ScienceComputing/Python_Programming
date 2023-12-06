A programming language can be either object-oriented or procedural, or both.

## Procedural programming
In the realm of programming, we often perceive code as a sequence of steps that guide a computer in executing tasks. Procedural programming, in particular, finds its niche when it comes to handling data analysis and creating scripts. One of its defining features is its inclination to prompt us to ponder the fundamental question: What is the intended objective of this program? This approach emphasizes a step-by-step, logical progression in designing and implementing software solutions.

## Object-oriented programming
In object-oriented programming (OOP), we view code as interactions between objects. This approach is particularly well-suited for constructing frameworks and tools, including application program interfaces and graphical user interfaces, as well as working with structures like pandas DataFrames. OOP helps us enhance the organization of our code, making it more reusable and easier to maintain. It encourages us to think about the environment created by a program, the entities within it, and how they collaborate. This holistic perspective fosters a deeper understanding of the software's design and functionality.

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

# Keep track of all the public and non-public methods and attributes of a class associated with an object
dir(obj)
```

- Best practices
  - Use `__init__()` to define all attributes in one place
  - Use `CamelCase` to define the name of a class, use `lower_snake_case` to define functions and attributes
  - Keep `self` as `self`
  - Use docstrings to show the function of a class
  - Use `dir` primarily at an interactive prompt, not in scripts

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
        if intron_length >= IntronicVariant.min_intron_length: # Use ClassName.attrite_name to access the class-level attribute value
            self.intron_length = intron_length
        else:
            self.intron_length = IntronicVariant.min_intron_length # Use ClassName.attrite_name to access the class-level attribute value

variant_1 = IntronicVariant('Gene_XYZ', 'Intron 3', 'A common intronic variant associated with disease M', 10)
variant_1.min_intron_length # 20
variant_1.intron_length # 20
```

## Class-level attributes
- By using the class attributes, we can set up the global constants related to the class, for example, min and max values for attributes or commonly used values (e.g., $\pi$, Euler's number, Planck's constant).
- By changing the value of a class attribute, we change the value of this class attribute for all instances associated with a class.

```
variant_1 = IntronicVariant('Gene_XYZ', 'Intron 3', 'A common intronic variant associated with disease M', 10)
IntronicVariant.min_intron_length = 25
variant_1.min_intron_length # 25
variant_1.intron_length # 25
```

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
    @classmethod # A decorator
    def class_method(cls): # Notice cls, not self; cls refers to a class
        cls.class_variable += 1
        print(f"Class method called. Class variable is now: {cls.class_variable}")

# Create instances of MyClass
obj1, obj2 = MyClass(1), MyClass(2)

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
            data = f.readline().strip().split(':') # strip() removes any extra whitespace at the beginning or end of the line
            name = data[0]
            intronic_variant = data[1] if len(data) > 1 else cls.DEFAULT_INTRONIC_VARIANT
        return cls(name, intronic_variant)

help(Gene)
gene = Gene.from_file("ClinVar_data.txt")
print(gene.name) # Output: BRCA1
print(gene.intronic_variant) # Output: c.5277+1G>A
```

## Class inheritance
```
The new class functionality is an extension of the existing class functionality, with the addition of extra features.
```
In the context of inheritance, a child class inherits **ALL** characteristics from a parent class and can also extend or modify those characteristics in some manner. For example, an `IntronicVariant` class is essentially a specialized type of `Variant` class; `Variant` serves as the fundamental or overarching class. This relationship can be described as an 'is-a' relationship, meaning that an `IntronicVariant` is a specific type of `Variant`.

Inheritance is a valuable feature in OOP languages, enabling us to tailor the functionality of existing classes without the need to start re-implement methods from scratch.

Inheritance allows class attributes to be passed down, and it's possible to modify the values of these class attributes in the child class.

```
class Variant:
    def __init__(self, chrom, position, ref, alt):
        self.chrom = chrom
        self.position = position
        self.ref = ref
        self.alt = alt
    def describe(self):
        return f"Variant at {self.chrom}:{self.position} ({self.ref}->{self.alt})"
    def annotate(self):
        return "No annotation available for this variant"

class IntronicVariant(Variant):
    def __init__(self, chrom, position, ref, alt, gene_name):
        super().__init__(chrom, position, ref, alt) #!
        self.gene_name = gene_name
    def describe(self):
        return f"Intronic Variant at {self.chrom}:{self.position} in {self.gene_name} ({self.ref}->{self.alt})"
    def annotate(self, annotation):
        return f"This variant in {self.gene_name} is: {annotation}"

variant = Variant("chr17", "43057051 (GRCh38)", "G", "A")
print(variant.describe())
print(variant.annotate())

intronic_variant = IntronicVariant("chr17", "43057051 (GRCh38)", "G", "A", "BRCA1")
print(intronic_variant.describe())
print(intronic_variant.annotate("Located in an intron"))
```

We use `super().__init__(chrom, position, ref, alt)` to call the constructor of the base class (Variant) instead of explicitly referencing `Variant.__init__(self, chrom, position, ref, alt)`. `super().__init__(...)` is a more modern and recommended way to call the base class constructor.

## Multilevel and multiple inheritance
- Multilevel inheritance occurs when a class inherits from another class, which itself inherits from another class, and so on. This creates a hierarchy of classes, where each class inherits the features of its parent class.
- Multiple inheritance occurs when a child class inherits from more than one parent class. This allows the child class to inherit all the features of its parent classes. However, this can also lead to ambiguity, as the child class may have multiple methods or attributes with the same name.

| Feature | Multilevel Inheritance | Multiple Inheritance |
|---|---|---|
| Number of base classes | One | Two or more |
| Inheritance hierarchy | Chain-like | Network-like |
| Complexity | Lower | Higher |
| Ambiguity | Lower | Higher |

## Object comparison
```
class Variant:
    def __init__(self, chrom, position, ref, alt):
        self.chrom = chrom
        self.position = position
        self.ref = ref
        self.alt = alt
    def describe(self):
        return f"Variant at {self.chrom}:{self.position} ({self.ref}->{self.alt})"
    def annotate(self):
        return "No annotation available for this variant"

variant_1 = Variant("chr17", "43057051 (GRCh38)", "G", "A")
variant_2 = Variant("chr17", "43057051 (GRCh38)", "G", "A")
variant_1 == variant_2 # False

class Variant:
    def __init__(self, chrom, position, ref, alt):
        self.chrom = chrom
        self.position = position
        self.ref = ref
        self.alt = alt
    def describe(self):
        return f"Variant at {self.chrom}:{self.position} ({self.ref}->{self.alt})"
    def annotate(self):
        return "No annotation available for this variant"
    def __eq__(self, other):
        print("__eq__() is called")
        return (self.chrom == other.chrom) and (self.position == other.position) and (self.ref == other.ref) and (self.alt == other.alt)

variant_1 = Variant("chr17", "43057051 (GRCh38)", "G", "A")
variant_2 = Variant("chr17", "43057051 (GRCh38)", "G", "A")
variant_1 == variant_2 # True  
```

## Polymorphism
Polymorphism involves employing a single interface to perform operations on objects belonging to various classes. Polymorphism guarantees that the exact method called is determined dynamically according to the instance.
```
class Shape:
    def describe(self):
        print("This is a shape.")

class Circle(Shape):
    def describe(self):
        print("This is a circle.")

class Triangle(Shape):
    def describe(self):
        print("This is a triangle.")
        Shape.describe(self)

shape_obj = Shape()
circle_obj = Circle()
triangle_obj = Triangle()

for obj in (shape_obj, circle_obj, triangle_obj):
    obj.describe()

# This is a shape.
# This is a circle.
# This is a triangle.
# This is a shape.
```

## [Liskov substitution principle](https://www.youtube.com/watch?v=-Z-17h3jG0A)
The following situations violate the Liskov substitution principle.
- While the method in the parent class requires only one parameter, the corresponding method in the subclass is designed to take two parameters.
- The subclass's method introduces additional constraints on the input parameters compared to its parent class counterpart.
- Compared to the method in the parent class, the method in the subclass imposes fewer restrictions on its output.
- The subclass's method introduces changes in additional attributes compared to its parent class counterpart.
- The subclass's method raises more exceptions compared to its parent class counterpart.
