## Selection sort algorithm
- Selection sort is a sorting technique that, during each iteration, picks the smallest element from an unsorted list and positions it at the start of the unsorted list.
- Its worst-case, average-case, best-base complexity is $O(n^2)$, $theta(n^2)$, and $\Omega(n^2)$, respectively.

```
def selection_sort(my_list):
    list_length = len(my_list)
    for i in range(list_length - 1):
        lowest = my_list[i]
        index = i
        for j in range(i + 1, list_length):
            if my_list[j] < lowest:
                index = j
                lowest = my_list[j]
        my_list[i], my_list[index] = my_list[index], my_list[i]
    return my_list
```
