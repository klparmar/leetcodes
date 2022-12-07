class Solution:
    def lengthOfLastWord(self, s: str) -> int:
    
        found = False;
        i = len(s) - 1;
        cnt = 0
        
        while not found or s[i] != " ":
            if s[i] != " ":
                found = True
            
            if found:
                cnt +=1
            
            i -=1;
            
            if i < 0:
                return cnt
            
        return cnt
        
