## Bubble sorting algorithms
- Sorting algorithms are crucial because they can reduce the complexity of problems.
- Bubble sorting algorithm examines and exchanges two neighboring elements until they are arranged correctly. Its worst case complexity is $O(n^2)$. Its best case complexity is $\Omega(n^2)$, when the list is already sorted. 
- Process:
  - Initial iteration: begin with the first index and compare it with the second element. If the first element is larger than the second, swap them. Continue this process for the second and third elements, swapping if necessary. Repeat these steps until reaching the last element.
  - Subsequent iterations: repeat the same process for the remaining iterations. After each iteration, the largest element among the unsorted ones is moved to the end. During each iteration, comparisons are made up to the last unsorted element. The array is considered sorted when all unsorted elements are in their correct positions.

```
def bubble_sort(my_list):
    list_length = len(my_list)
    for i in range(list_length-1):
        for j in range(list_length-1-i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list

print(bubble_sort([6,1,2,3,7])) # [1, 2, 3, 6, 7]

# for j in range(list_length-1-i): with each pass, the largest number in the remaining part of the list bubbles up to its correct position, so there is no need to check it again.
```

- Optimize the bubble sorting algorithm so that it can detect the list which is already sorted and terminate the execution. Its best case complexity is $\Omega(n)$, when the list is already sorted.  
```
def bubble_sort_optimize(my_list):
    list_length = len(my_list)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(list_length-1):
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                is_sorted = False
        list_length -= 1
    return my_list

# for i in range(list_length-1): if no swaps are made during a full pass of the inner loop (meaning no elements are out of order), the is_sorted flag remains True, which indicates that the list is sorted. Consequently, the while loop condition while not is_sorted: becomes False, and the loop exits.
```
