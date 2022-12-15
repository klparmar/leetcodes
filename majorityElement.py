class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dictt = {}

        for i in nums:
            if i not in dictt:
                dictt[i] = 1
            else:
                dictt[i] += 1

        for i in dictt:
            if dictt[i] >= (len(nums) / 2):
                return i
