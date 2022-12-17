class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        curr = math.inf

        result = [-1] * len(nums1)

        for i in range(len(nums1)):
            for j in nums2:
                if j == nums1[i]:
                    curr = j
                if j > curr:
                    result[i] = j
                    break
                    
            curr = math.inf
        return result
