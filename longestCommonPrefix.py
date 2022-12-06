class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for i in strs:
            for j in range(len(prefix)):
                if len(i) <= j:
                    prefix = i
                elif i[j] != prefix[j]:
                    prefix = prefix[:j]
                    break

        return prefix
