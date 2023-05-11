"""
The reason for this is that in each iteration of the outer loop (which iterates i times), the largest i elements of the array have already 
been sorted and placed at the end of the array. Therefore, we don't need to compare these elements again in subsequent iterations of the 
inner loop.

So, in each iteration of the inner loop, we can compare the current element at index j with the next element at index j+1, up until the 
second-last element in the unsorted portion of the array, which is at index n-i-2. The n-i-1 value represents the length of the unsorted portion of the array at the beginning of each iteration of the outer loop, minus 1 to account for zero-based indexing.

For example, in the first iteration of the outer loop, i is 0, so we need to compare all n elements of the array. In the 
second iteration, i is 1, so we can skip comparing the last element (which has already been sorted in the previous iteration) and only 
compare the first n-1 elements. In the third iteration, i is 2, so we can skip comparing the last two elements and only compare the 
first n-2 elements, and so on.
"""


def sortArray(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(sortArray([2, 5, 1]))
