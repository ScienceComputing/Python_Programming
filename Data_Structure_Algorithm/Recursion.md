- What is recursion?
  - Recursion is the function calling itself
  - We can substitute the most loops with recursion

```
# Factorial example
def factorial(n):
  outcome = 1
  while n > 1:
    outcome = n * outcome
    n -= 1
  return outcome

factorial(3)
# 6
```

- How to develop recursion algorithm?
  - Add a condition to ensure that our algorithm does not execute forever
  - Define a factorial base case (n = 1), such that we will not make any recursive calls
  - If n > 1, we make recursive calls
```
def factorial_recursion(n)
  if n == 1:
    return 1
  else:
    return n * factorial_recursion(n - 1)

factorial_recursion(6)
# 3
```

- How does recursion work?
  - Use a [stack](Stack.md) to keep track of the functions; this stack is the call stack.
  - factorial(3) starts; before factorial(3) finishes, factorial(2) starts; before factorial(2) finishes, factorial(1) starts; factorial(1) finishes, returning 1
  - factorial(2) finishes, returning 2 (2 * factorial(1)); factorial(3) finishes, returning 6 (3 * factorial(2))

- Dynamic programming
  - An optimization technique mainly applied to recursion
  - Reduce the complexity of recursive algorithms
  - Used for any problem that can be divided into smaller subproblems that overlap
  - The solutions of the subproblems are saved, avoiding recalculating them if needed later. This can be done with the memoization technique
 
```
# Fibonacci example: Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones; e.g., 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
def fibonacci(n):
  # Define the base case
  if n <= 1:
    return n
  else:
    # Call recursively to fibonacci
    return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(6))

# Use the dynamic problem to save the solutions of the subproblems in the cache variable, to avoid recalculating it later
cache = [None]*(100)

def fibonacci(n): 
    if n <= 1:
        return n
    if not cache[n]: # Check if the value exists
        cache[n] = fibonacci(n-1) + fibonacci(n-2) # Save the result in cache
    return cache[n]
    
print(fibonacci(6))
```
