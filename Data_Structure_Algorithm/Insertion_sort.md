## Insertion sort algorithm
- Insertion sort is a sorting technique that, during each iteration, positions an unsorted element into its appropriate location.
- Its worst-case, average-case, best-base complexity is $O(n^2)$, $\Theta(n^2)$, and $\Omega(n)$, respectively.

```
# TD
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        number_to_order = my_list[i]
        j = i - 1
        while j >= 0 and number_to_order < my_list[j]:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = number_to_order
    return my_list
```
