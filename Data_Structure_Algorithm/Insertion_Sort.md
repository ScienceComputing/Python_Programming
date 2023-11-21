## Insertion sort algorithm
- Insertion sort is a sorting technique that, during each iteration, positions an unsorted element into its appropriate location.
- Its worst-case, average-case, best-base complexity is $O(n^2)$, $\Theta(n^2)$, and $\Omega(n)$, respectively.

```
def insertion_sort(my_list):
    for i in range(1, len(my_list)): # Start from the second element (index 1) to the end of the list (len(my_list)), since the first element is considered sorted by default
        number_to_order = my_list[i]
        j = i - 1 # j as the index of the element just before the current element. j will be used to compare number_to_order with my_list[j]
        while j >= 0 and number_to_order < my_list[j]: # This is the condition to find the correct position for number_to_order.
            my_list[j + 1] = my_list[j] # If the condition is true, the element at my_list[j] is moved one position to the right to make space for number_to_order.
            j -= 1
        my_list[j + 1] = number_to_order
    return my_list
```
*The insertion_sort algorithm sorts a list by iterating over each element, starting from the second one, and inserting it into the correct position within the sorted portion of the list to the left. During each iteration, it compares the current element with the sorted elements and shifts the sorted elements to the right to create space, as needed. This process is repeated until the whole list is sorted, resulting in a rearranged list where each item is in its proper order, from the lowest to the highest. This algorithm is efficient for sorting small lists and performs well when the list is already partially sorted.*
