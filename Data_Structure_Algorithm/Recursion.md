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
  - Use a stack to keep track of the functions
  
