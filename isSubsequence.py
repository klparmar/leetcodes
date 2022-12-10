class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        index = 0
        if s == "":
            return True

        for i in t:
            if i == s[index]:
                index +=1
                
            if index == len(s):
                return True
            
        return index == len(s)
