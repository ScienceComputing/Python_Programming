# Formatting rule for the import
- Import statements should be employed exclusively for packages and modules, avoiding their use for individual classes or functions.
- `a.xyz` asserts that the module a defines the object named xyz.
- To import packages and modules, please use `import a`.
- Please use `from a import b`, where 'a' represents the package prefix, and 'b' signifies the module name without any prefix.
- Only when b is a standard abbreviation (e.g., import pandas as pd), use `import a as b`

