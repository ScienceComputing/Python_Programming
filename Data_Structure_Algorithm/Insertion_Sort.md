## Insertion sort algorithm
- Insertion sort is a sorting technique that, during each iteration, positions an unsorted element into its appropriate location.
- Its worst-case, average-case, best-case complexity is $O(n^2)$, $\Theta(n^2)$, and $\Omega(n)$, respectively.

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

- Start with the second element (3): compare 3 with the first element 4. Since 3 is less than 4, swap them. Now the list looks like [3, 4, 7, 2].
- Move to the third element (7): compare 7 with the previous element 4. No swap is needed because 7 is greater than 4. The list remains [3, 4, 7, 2].
- Move to the fourth element (2): compare 2 with the previous element 7. 2 is less, so swap 2 and 7. Now the list is [3, 4, 2, 7]. Now compare 2 with 4. Again, 2 is less, so swap 2 and 4. The list is now [3, 2, 4, 7]. Compare 2 with 3. 2 is less, so swap 2 and 3. The list becomes [2, 3, 4, 7].

```
my_list[j + 1] = number_to_order
```

This code means we're placing the value we're sorting (number_to_order) into its correct position in the list.

When we get to the point of inserting 2:
- Start with 2 as number_to_order and compare it with 7. Since 2 is smaller, we move 7 one spot to the right. Now our list looks like [3, 4, 7, 7], and we have j pointing to 4.
- Next, compare 2 with 4. It's smaller again, so we move 4 to the right where 7 was. The list is now [3, 4, 4, 7], and j moves to the 3.
- 2 is still smaller than 3, so we move 3 to the right. The list is [3, 3, 4, 7].
- Now we've reached the start of the list, and **j is -1** (j -= 1). It's time to insert 2.
- `my_list[j + 1] = number_to_order` takes 2 and puts it in the position right after where j is pointing, which is the start of the list. So we get [2, 3, 4, 7].
