def findMedianSortedArrays(nums1: [int], nums2: [int]) -> float:
    array = sorted(nums1 + nums2) # add 2 arrays together using python's built in method lol
    mid = len(array) // 2 # find midpoint

    if len(array) % 2 == 0: # if midpoint is even
        return (array[mid - 1] + array[mid]) / 2 # return avg of 2 midpoints
    return array[mid] # return midpoint

assert findMedianSortedArrays([1,3], [2]) == 2.0
assert findMedianSortedArrays([1,2], [3,4]) == 2.5
