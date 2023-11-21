## Quick sort algorithm
- Quicksort adheres to the divide and conquer approach. This sorting algorithm employs a partitioning technique in which it selects a value, known as the pivot, from the list. It arranges all items smaller than the pivot to its left and places greater elements to its right. Quicksort proceeds to recursively call itself on the elements located to the left and right of the pivot.

```
# TD
def quicksort(my_list, first_index, last_index):
    if first_index < last_index:
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
