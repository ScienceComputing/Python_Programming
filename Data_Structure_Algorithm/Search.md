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
