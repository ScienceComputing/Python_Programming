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
- Encapsulation is a distinctive feature of OOP, which bundles the attributes with the methods operating on them
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

