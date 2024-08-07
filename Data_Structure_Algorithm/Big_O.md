## Table of Contents

* [Complexity of an algorithm](#Complexity-of-an-algorithm)
* [Big O notation](#Big-O-notation)
* [Big omega notation](#Big-omega-notation)
* [Big theta notation](#Big-theta-notation)
* [Typical time complexity](#Typical-time-complexity)
* [Simplify the big O notation](#Simplify-the-big-O-notation)
* [Space complexity](#Space-complexity)



## Complexity of an algorithm
We need a metric for estimating algorithm efficiency and assessing algorithm quality that is independent of external factors like hardware/software performance and scale. Complexity analysis inherently serves this purpose.

## Big O notation
- It measures the worst-case complexity of an algorithm: how the increase in the input size increases the time taken to execute an algorithm.
    - **Time complexity $T(n)$**: time taken to run completely
    - **Space complexity $S(n)$**: extra memory space required by an algorithm
- We do not use seconds/bytes to quantify the complexity of an algorithm, as different time/space complexities depend on the hardware/software settings.
- We use the mathematical symbols to express the complexity: $O(1)$, $O(n)$, $O(n^2)$.

When describing the speed of an algorithm in terms of its runtime, the **total number of steps executed in the algorithm** becomes particularly important. We can assume that the runtime of each line of code is represented by a constant `Btime`. Therefore, the total runtime of the algorithm equals the total number of lines of code executed.

## Big omega notation
- It measures the **best-case** complexity of an algorithm: how the increase in the input size increases the time taken to execute an algorithm.

## Big theta notation
- It measures the **average-case** complexity of an algorithm: how the increase in the input size increases the time taken to execute an algorithm.

```
def search_word(word_list, target_word): 
    for i in range(len(word_list)):        
        if word_list[i] == target_word:
            break
```

The variable `target_word` can appear at any position within the list `word_list`, where this list is given as `['FIJI', 'Evian', 'Poland Spring', 'Essentia']`:

- When `target_word` is `FIJI`, it matches the first item in the `word_list`, and there is no need to traverse the rest of the list. In this case, the time complexity is $O(1)$, which is the **best-case** complexity.
- When `target_word` is `Essentia` or any non-existent `VOSS`, the entire list is traversed. In these two scenarios, the time complexity is $O(n)$, which is the **worse-case** complexity.
- The **average-case** complexity is $\frac{1}{2n} + \frac{2}{2n} + \frac{3}{2n} + \cdots + \frac{n}{2n} + \frac{n}{2} = \frac{3n+1}{4}$ -> $O(n)$.
- In most cases, we do not need to distinguish between best-case, worst-case, and average-case time complexity. We only differentiate these three cases when the same piece of code exhibits significant variations in time complexity under different cases. This is done to describe the time complexity of the code more effectively.

## Typical time complexity

```diff
- We focus on Time Complexity
```

| Name                       | Complexity   | Total number of steps executed by the algorithm |
|----------------------------|--------------|-----------------------|
| Constant Time Complexity   | $O(1)$         | $1$                     |
| Logarithmic Time Complexity| $O(logn)$      | $logn + 1$              |
| Linear Time Complexity     | $O(n)$        | $n + 1$                 |
| Linearithmic Time Complexity| $O(nlogn)$    | $nlogn + 1$             |
| Polynomial Time Complexity | $O(n^2)$, $O(n^3)$, ... | $n^2 + n + 1$         |
| Exponential Time Complexity| $O(2n)$        | $2n + 1$                |
| Factorial Time Complexity  | $O(n!)$        | $n! + 1$                |

### O(1) - constant
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

### O(n) - linear
```
variant_index = [0, 1, 2, 3]
variant_index_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def print_element(object):
    for i in object:
        print(i)

print_element(variant_index) # o(4)

print_element(variant_index_2) # o(9)
```

### O(n^2) - quadratic
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

### O(n^3) - cubic
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

### O(logn) - logarithmic
Let us initialize `var1` to 1, and determine how many times it needs to be multiplied by 2 to become greater than or equal to $n$. $2^{times} \ge n$. $Times$ = $log_2{n}$.
```
var1 = 1
while var1 < n:    
    var1 = var1 * 2 
```

### O(nlogn) - linearithmic
```
def custom_count(n):    
    count = 0    
    for j in range(n):      
        my_var = 1 # 
        
        while my_var < n:            
            my_var = my_var * 2 #         
            count += 1    
    return count
```

## Simplify the big O notation
- Remove the constants: $O(2 + m + 2n)$ -> $O(m + n)$
- Consider different variables for different inputs: $O(m + n)$
- Remove the smaller term: $O(n^2 + n)$ -> $O(n^2)$
- $O(log_2{n})$ = $O(log_2{any \ number} \times log_{any \ number}{n})$ = $O(log_{any \ number}{n})$ -> $O(logn)$

## Space complexity
- Space complexity, like time complexity, reflects a trend, but it pertains to the amount of memory space the temporary variables occupy during the execution of the code.

### O(1)
```
def calculate_sum(numbers):    
    result = 0    
    for num in numbers:        
        result += num
    return result
```
The temporary variables are `result` and `num`. `result` stores the sum of values, which is of constant order, and `i` stores the element in the `numbers`, which is also of constant order. The space allocated for these two variables is independent of the size $n$, so the overall space complexity of the code is $O(1)$.

### O(n)
```
def generate_list(n):
    my_list = []
    for num in range(n):
        my_list.append(num)
    return my_list
```
`my_list` is an initially empty list that occupies memory which increases with the growth of the for loop, reaching a maximum of `n`. Therefore, the space complexity of `my_list` is $O(n)$. `num` represents a constant-order storage for element positions, independent of the scale `n`. As a result, the space complexity of this code remains $O(n)$.

### O(n^2)
```
def create_list(n):
    result_list = []
    for i in range(n):
        inner_list = []
        for j in range(n):
            inner_list.append(j)
        result_list.append(inner_list)
    return result_list
```
- `result_list` stores `n` inner lists, each of which contains `n` integers. Therefore, the space required for `result_list` is $O(n^2)$.
- Each `inner_list` contains `n` integers, and there are `n` such inner lists created. Therefore, the space required for all `inner_list` instances is $O(n^2)$.
- Temporary variables `i` and `j` do not significantly contribute to the space complexity as they occupy constant space, $O(1)$.
- The dominant factor in the space complexity is the storage of the `result_list` and the `inner_list` instances, both of which scale with the square of the input value `n`, resulting in the overall $O(n^2)$ space complexity.
