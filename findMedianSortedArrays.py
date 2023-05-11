def findMedianSortedArrays(nums1, nums2) -> float:
    new_array = sorted(nums1 + nums2)
    median_index = len(new_array) // 2

    if len(new_array) % 2 == 0:
        temp = (new_array[median_index] + new_array[median_index-1])/2
        return temp
    else:
        return float(new_array[median_index])


print(findMedianSortedArrays([1, 3], [2]))
print(findMedianSortedArrays([1, 2], [3, 4]))
