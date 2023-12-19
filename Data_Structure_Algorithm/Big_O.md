## Complexity of an algorithm
We need a metric for estimating algorithm efficiency and assessing algorithm quality that is independent of external factors like hardware/software performance and scale. Complexity analysis inherently serves this purpose.

## Big O notation
- It measures the worst-case complexity of an algorithm: how the increase in the input size increases the time taken to execute an algorithm.
    - **Time complexity**: time taken to run completely
    - Space complexity: extra memory space required by an algorithm
- We do not use seconds/bytes to quantify the complexity of an algorithm, as different time/space complexities depend on the hardware/software settings.
- We use the mathematical symbols to express the complexity: $O(1)$, $O(n)$, $O(n^2)$.

When describing the speed of an algorithm in terms of its runtime, the **total number of steps executed in the algorithm** becomes particularly important. We can assume that the runtime of each line of code is represented by a constant `Btime`. Therefore, the total runtime of the algorithm equals the total number of lines of code executed.

## Typical time complexity

```diff
- We focus on Time Complexity
```

| Name                       | Complexity   | Total number of steps executed by the algorithm |
|----------------------------|--------------|-----------------------|
| Constant Time Complexity   | $O(1)$         | 1                     |
| Logarithmic Time Complexity| $O(logn)$      | $logn$ + 1              |
| Linear Time Complexity     | $O(n)$        | $n$ + 1                 |
| Linearithmic Time Complexity| $O(nlogn)$    | $nlogn$ + 1             |
| Polynomial Time Complexity | $O(n^2)$, $O(n^3)$, ... | $n^2$ + $n$ + 1         |
| Exponential Time Complexity| $O(2n)$        | $2n$ + 1                |
| Factorial Time Complexity  | $O(n!)$        | $n!$ + 1                |


## Big omega notation
- It measures the best-case complexity of an algorithm: how the increase in the input size increases the time taken to execute an algorithm.

## Big theta notation
- It measures the average-case complexity of an algorithm: how the increase in the input size increases the time taken to execute an algorithm.

## O(1) - constant
The increase in the input size does not change the time taken to execute an algorithm.
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

## O(n^3) - cubic
```
variant_index = [0, 1, 2, 3]

def print_element(object):
    for i in object:
        for j in object:
            for k in object:
                print(i, j, k)

print_element(variant_index) # o(64)
```

Another example below:
```
def custom_sum(n):    
    sum1 = 0    
    for var1 in range(n):        
        sum1 += var1

    sum2 = 0    
    for var2 in range(n):        
        for i in range(n):            
            sum2 += var2 * i
    
    sum3 = 0    
    for var3 in range(n):        
        for i in range(n):            
            for j in range(n):                
                sum3 += var3 * i * j

    return sum1 + sum2 + sum3
```
Normally, $T(n)$ = $O(n)$ + $O(n^2)$ + $O(n^3)$. However, when $n$ approaches infinity, it's evident that the first two terms can be disregarded, leaving us with a final complexity of $T(n)$ = $O(n^3)$.

## O(logn) - logarithmic
Let us initialize `var1` to 1, and determine how many times it needs to be multiplied by 2 to become greater than or equal to $n$. $2^{times} \ge n$. $Times$ = $log_2{n}$.
```
var1 = 1
while var1 < n:    
    var1 = var1 * 2 
```

## Simplify the big O notation
- Remove the constants: $O(2 + m + 2n)$ -> $O(m + n)$
- Consider different variables for different inputs: $O(m + n)$
- Remove the smaller term: $O(n^2 + n)$ -> $O(n^2)$
- $O(log_2{n})$ = $O(log_2{any number} \times log_{any number}{n})$ = $O(log_{any number}{n})$ = $O(logn)$

## [TD] More examples
