## Merge sort algorithm
- Merge sort adheres to the divide and conquer approach. It works by [recursively](Recursion.md) splitting the input list into smaller halves, sorting those halves, and then merging them back together to produce a sorted list.
  - It begins with the **divide** phase, where the problem is divided into smaller, manageable sub-problems.
  - Next, during the **conquer** phase, these sub-problems are solved recursively.
  - Finally, in the **combine** phase, the solutions to these sub-problems are integrated to obtain the ultimate solution.
- Its complexity is $O(n log n)$, which is a significant improvement over bubble sort, selection sort, and insertion sort, which have a complexity of $O(n^2)$. Hence, merge sort is suitable for sorting large lists of numbers. In average and best cases, it also has a complexity of $O(n log n)$. Other algorithms like bubble sort or insertion sort have better best case complexity $\Omega(n)$.
- Its space complexity $O(n)$, as it needs extra space to treat the two halves. The other algorithms have space compexity $O(1)$.

```
def merge_sort(my_list): # Input a list to sort
    if len(my_list) > 1: # A list with zero or one element is inherently sorted
        mid = len(my_list)//2 # Floor division of the length of my_list by 2
        left_half = my_list[:mid] # Elements from the start of my_list up to (but not including) the mid index
        right_half = my_list[mid:] # Elements from the mid index to the end of my_list
        merge_sort(left_half)
        merge_sort(right_half) # Recursively divide the list until each left/right list has only one element
        i = j = k = 0 # Proceed to merge the sorted parts. Declare the i variable for the index of the left_half, the j variable for the index of the right_half, and the k variable for the index of the final list
        while i < len(left_half) and j < len(right_half): 
            if left_half[i] < right_half[j]: # Compare elements at indices i and j in left_half and right_half
                my_list[k] = left_half[i] # Add the smaller element to the my_list at index k
                i += 1 # It then increments the index variable i
            else: # if left_half[i] >= right_half[j]
                my_list[k] = right_half[j]
                j += 1 # It then increments the index variable j
            k += 1 # It then increments the index variable k

        # The following 2 while loops are responsible for copying any remaining elements from the left_half and right_half sub-lists into the final merged list, ensuring that no elements are left out during the merging process
        while i < len(left_half):
            my_list[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            my_list[k] = right_half[j]
            j += 1
            k += 1

list_1 = [12, 11, 46, 29, 3, 1, 77, 0, 108]
merge_sort(list_1)
print(list_1) # [0, 1, 3, 11, 12, 29, 46, 77, 108]
```
