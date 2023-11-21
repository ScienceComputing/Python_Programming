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

Let's walk through the insertion_sort algorithm using the list [4, 3, 7, 2]:

- Start with the second element (3): compare 3 with the first element 4.Since 3 is less than 4, swap them. Now the list looks like [3, 4, 7, 2].
- Move to the third element (7): compare 7 with the previous element 4. No swap is needed because 7 is greater than 4. The list remains [3, 4, 7, 2].
- Move to the fourth element (2): compare 2 with the previous element 7. 2 is less, so swap 2 and 7. Now the list is [3, 4, 2, 7]. Now compare 2 with 4. Again, 2 is less, so swap 2 and 4. The list is now [3, 2, 4, 7]. Compare 2 with 3. 2 is less, so swap 2 and 3. The list becomes [2, 3, 4, 7].
