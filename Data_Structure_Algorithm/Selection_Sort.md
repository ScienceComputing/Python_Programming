## Selection sort algorithm
- Selection sort is a sorting technique that, during each iteration, picks the smallest element from an unsorted list and positions it at the start of the unsorted list.
- Its worst-case, average-case, best-base complexity is $O(n^2)$, $\Theta(n^2)$, and $\Omega(n^2)$, respectively.

```
def selection_sort(my_list):
    list_length = len(my_list)
    for i in range(list_length - 1):
        lowest = my_list[i] # Set lowest to the element of the list located at index i
        index = i
        for j in range(i + 1, list_length): # Iterate again over the list starting on the next position of the i variable
            if my_list[j] < lowest: # Compare whether the element of the list located at index j is smaller than lowest
                index = j
                lowest = my_list[j]
        my_list[i], my_list[index] = my_list[index], my_list[i]
    return my_list

list_1 = [9, 1, 2, 3, 1, 7] 
selection_sort(list_1)
print(list_1) # [1, 1, 2, 3, 7, 9]
```
