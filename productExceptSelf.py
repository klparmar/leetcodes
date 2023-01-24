class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        prod = 1
        for i in range(len(nums)):
            prod = prod * nums[i]
            ans[i] = prod

        ans2 = [0] * len(nums)
        prod = 1

        for i,x in enumerate(reversed(nums)):
            prod = prod * x
            ans2[i] = prod
        ans2 = ans2[::-1]

        finalAns = [0] * len(nums)

        for i in range(len(nums)):
            pre = i - 1
            post = i + 1
            if pre < 0:
                pre = 1
            else:
                pre = ans[pre]

            if post == len(nums):
                post = 1
            else:
                post = ans2[post]
            
            finalAns[i] = pre * post
            
        return finalAns
