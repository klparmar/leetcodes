class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        x = len(s) - 1
        temp = ""
        while i<x:
            temp = s[i]
            s[i] =s[x]
            s[x] = temp
        
            i+=1
            x-=1

        
