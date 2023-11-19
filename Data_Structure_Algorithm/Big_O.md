## Big O Notation
- It measures the worst-case complexity of an algorithm: how the increase in the input size increases the time taken to execute an algorithm
  - **Time complexity**: time taken to run completely [focus]
  - Space complexity: extra memory space
  ```diff
  - Time complexity: time taken to run completely [focus]
  ```
- Doesn't use seconds/bytes: different results depend on the hardware settings
- Use the mathematical symbols to express the complexity: $O(1)$, $O(n)$, $O(n^2)$

```diff
- Time complexity
```

## O(1) - constant
```
variant_index = [0, 1, 2, 3]
variant_index_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def retrieve(object):
    print(object[1])

retrieve(variant_index)
# 1

retrieve(variant_index_2)
# 1
```

## O(n) - linear
```
variant_index = [0, 1, 2, 3]
variant_index_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def print_element(object):
    for i in object:
        print(i)

print_element(variant_index) # o(4)

print_element(variant_index_2) # o(9)
```

## O(n^2) - quadratic
```
variant_index = [0, 1, 2, 3]
variant_index_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def print_element(object):
    for i in object:
        for j in object:
            print(i, j)

print_element(variant_index) # o(16)

print_element(variant_index_2) # o(81)
```

## O(n^2) - cubic
```
variant_index = [0, 1, 2, 3]

def print_element(object):
    for i in object:
        for j in object:
            for k in object:
                print(i, j, k)

print_element(variant_index) # o(64)
```

## Simplify the big O notation
- Remove the constants: $O(2 + m + 2n)$ -> $O(m + n)$
- Consider different variables for different inputs: $O(m + n)$
- Remove the smaller term: $O(n^2 + n)$ -> $O(n^2)$

## [TD] More examples
