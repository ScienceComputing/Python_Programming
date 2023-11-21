## Merge sort algorithm
- Merge sort adheres to the divide and conquer approach, which involves breaking the task down into several distinct phases.
  - It begins with the **Divide** phase, where the problem is divided into smaller, manageable sub-problems.
  - Next, during the **Conquer** phase, these sub-problems are solved recursively.
  - Finally, in the **Combine** phase, the solutions to these sub-problems are integrated to obtain the ultimate solution.
- Its complexity is O($n log n$), which is a significant improvement over bubble sort, selection sort, and insertion sort, which have a complexity of O($n^2$). Hence, merge sort is suitable for sorting large lists of numbers. In average and best cases, it also has a complexity of O($n log n$). Other algorithms like bubble sort or insertion sort have better best case complexity $\Omega(n)$.
- The inconvenience of this algorithm is its space complexity O($n$). 

```
Merge sort - implementation

def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list)//2
        left_half = my_list[:mid]
        right_half = my_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half) # Recursively divide the list until each left/right list has only one element

        i = j = k = 0 # Proceed to merge the sorted parts. Declare the i variable for the index of the left_half, the j variable for the index of the right_half, and the k variable for the index of the final list. 
        while i < len(left_half) and j < len(right_half): # TD
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i += 1
            else:
                my_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            my_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            my_list[k] = right_half[j]
            j += 1
            k += 1

        my_list = [35, 22, 90, 4, 50, 20, 30, 40, 1]
        merge_sort(my_list)
        print(my_list)

```
