class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        x = len(s) - 1
        flag = True
        
        while i < x:
            if s[i] != s[x]:
                j = i
                z = x - 1
                
                while j < z:
                    if s[j] != s[z]:
                        flag = False
                        break
                    j += 1
                    z -= 1
                    
                if not flag:
                    j = i + 1
                    z = x
                    while j < z:
                        if s[j] != s[z]:
                            flag = True
                            break
                        j += 1
                        z -= 1
                        
                    if flag:
                        return False
                    else:
                        return True
                    
                else:
                    return True
                    
            i += 1
            x -= 1
        return True
      
#Runtime: 162 ms, faster than 80.31% of Python3 online submissions for Valid Palindrome II.
#Memory Usage: 14.5 MB, less than 46.62% of Python3 online submissions for Valid Palindrome II.
