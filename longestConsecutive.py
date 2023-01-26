class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sett = set()
        for i in nums:
            if i not in sett:
                sett.add(i)

        longest = 0
        length = 1
        for i in sett:
            if (i - 1) not in sett:
                while (i + length) in sett:
                    length +=1
                longest = max(length, longest)
                length = 0

        return longest
