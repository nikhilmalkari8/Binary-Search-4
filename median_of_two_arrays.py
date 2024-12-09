"Time Complexity is O(log(m+n))"
"Space Complexity is O(1)"

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        len1, len2 = len(nums1), len(nums2)
        left, right = 0, len1

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (len1 + len2 + 1) // 2 - partition1

            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == len1 else nums1[partition1]
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == len2 else nums2[partition2]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (len1 + len2) % 2 == 1:
                    return max(maxLeft1, maxLeft2)
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2

            if maxLeft1 > minRight2:
                right = partition1 - 1
            else:
                left = partition1 + 1
