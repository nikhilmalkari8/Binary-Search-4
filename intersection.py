"Time Complexity is O(N)"
"Space Complexity is O(N)"

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        mapofnums1 = Counter(nums1)
        
        for i in range(len(nums2)):
            if nums2[i] in mapofnums1 and mapofnums1[nums2[i]] !=0 :
                mapofnums1[nums2[i]] = mapofnums1[nums2[i]] - 1
                result.append(nums2[i])
        return result