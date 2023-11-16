# Searching algorithms
- Two algorithms that search for an element within a collection of elements: linear search and binary search
- Linear search: try to search for a value by **looping through each element** of the list; if the element is found, the algorithm stops and returns the result; otherwise, the algorithm continues; it has $O(n)$ complexity

```
def linear_search(list_obj, search_val):
  for id in range(len(list_obj)):
    if list[id] == search_val:
      return True
  return False
```

- Binary search: an efficient algorithm used to find the position of a target value within a sorted list. It works by repeatedly dividing the search interval in half and comparing the target with the middle element of the array until the target is found or the search space is exhausted; it has $O(log n)$ complexity, which is more computational efficient than the linear search when the input size is very large
```
def binary_search(ordered_list_obj, search_val):
  first = 0
  last = len(ordered_list_obj) - 1

  while first <= last:
    middle = (first + last) // 2
    if search_val == ordered_list_obj[middle]:
      return True
    elif search_val < ordered_list_obj[middle]:
      last = middle - 1
    else:
      first = middle + 1
  return False
```
