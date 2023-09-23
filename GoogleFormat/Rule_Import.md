# Formatting rule for the import
- We should use the import statements exclusively for packages and modules, avoiding their usage for individual classes or functions (e.g., from some_module import some_class).
- `a.xyz` asserts that the module a defines the object named xyz.
- To import packages and modules, please use `import a`.
- Please use `from a import b`, where 'a' represents the package prefix, and 'b' signifies the module name without any prefix.
- Only when b is a standard abbreviation (e.g., import pandas as pd), use `import a as b`
- We should use the syntax "from x import y as z" in any of the subsequent situations:
  1. When we need to import two modules with the name "y".
  2. When there's a clash between the name "y" and a top-level identifier in the current module.
  3. When the name "y" conflicts with a commonly used parameter name within the public API.
  4. When "y" is excessively long and cumbersome to use.
  5. When the name "y" is too generic in the specific context of our codes, for instance, when we are importing "options" from "storage.file_system" and need to use an alias like "fs_options" to avoid ambiguity (`from storage.file_system import options as fs_options`).

