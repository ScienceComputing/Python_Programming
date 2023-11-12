## Big O Notation
- It measures the worst-case complexity of an algorithm
  - Time complexity: time taken to run completely
  - Space complexity: extra memory space
- Doesn't use seconds/bytes: different results depend on the hardware
- Use the mathematical expression: $O(1)$, $O(n)$, $O(n^2)$

## O(1)
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
