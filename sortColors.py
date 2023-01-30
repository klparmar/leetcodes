class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        dictt = {}

        for i in reversed(range(len(nums))):
            if nums[i] not in dictt:
                dictt[nums[i]] = 1
            else:
                dictt[nums[i]] += 1
            nums.pop()

        for i in range(3):
            if i in dictt:
                for j in range(dictt[i]):
                    nums.append(i)
