class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1

        while p1<p2:
            if (numbers[p1] + numbers[p2]) < target:
                p1 +=1
            elif (numbers[p1] + numbers[p2]) > target:
                p2 -=1
            else:
                return [p1+1, p2+1]


# Runtime
# Details
# 115ms
# Beats 98.82%of users with Python3
# Memory
# Details
# 17.18mb
# Beats 94.37%of users with Python3
