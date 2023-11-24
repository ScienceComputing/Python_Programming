## Quick sort algorithm
- Quicksort adheres to the divide and conquer approach. This sorting algorithm employs a partitioning technique in which it selects a value, known as the pivot, from the list. It arranges all items smaller than the pivot to its left and places greater elements to its right. Quicksort then [recursively](Recursion.md) sorts the elements located to the left and right of the pivot.
- Its worst-case complexity is $O(n^2)$, while its average-case and best-case complexity are $\Theta(n \ log \ n)$ and $\Omega(n \ log \ n)$.
- Its space complexity is $O(n \ log \ n)$.

```
# TD
def quicksort(my_list, first_index, last_index):
    """
    my_list: the list to be sorted
    first_index: the index of the first element of the current sub-list
    last_index: the index of the last element of the current sub-list
    """
    if first_index < last_index: # Check if first_index is less than last_index. If not, the function returns without doing anything, as it's considered a **base case** for recursion
        partition_index = partition(my_list, first_index, last_index)
        quicksort(my_list, first_index, partition_index)
        quicksort(my_list, partition_index + 1, last_index)

def partition(my_list, first_index, last_index):
    pivot = my_list[first_index]
    left_pointer = first_index + 1
    right_pointer = last_index
    while True:
        while my_list[left_pointer] < pivot and left_pointer < last_index:
            left_pointer += 1
        while my_list[right_pointer] > pivot and right_pointer >= first_index:
            right_pointer -= 1
        if left_pointer >= right_pointer:
            break
        my_list[left_pointer], my_list[right_pointer] = my_list[right_pointer], my_list[left_pointer]
    my_list[first_index], my_list[right_pointer] = my_list[right_pointer], my_list[first_index]
    return right_pointer

list_1 = [5, 67, 2, 1, 199, 20, 50]
quicksort(list_1, 0, len(list_1) - 1)
print(list_1) # [1, 2, 5, 20, 50, 67, 199]

```
