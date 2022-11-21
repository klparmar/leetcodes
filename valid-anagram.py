class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        setTing = {}
        
        for i in s:
            if i in setTing:
                setTing[i] += 1
            else:
                setTing[i] = 1
        
        for j in t:
            if j not in setTing:
                return False
            else:
                setTing[j] -= 1
                
        for x in setTing:
            if setTing[x] != 0:
                return False
            
        return True