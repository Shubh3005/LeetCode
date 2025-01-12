import heapq
def findMedianSortedArrays(nums1,nums2):
    while len(nums1) > len(nums2):
        nums1.pop()
    while len(nums2) > len(nums1):
        nums2.pop()
    nums1.extend(nums2)
    heapq.heapify(nums1)
    n = len(nums1)
    return nums1[n//2] if n%2 else (nums1[n//2-1]+nums1[n//2])/2
print(findMedianSortedArrays([1,3],[2]))
print(findMedianSortedArrays([1,2],[3,4]))         