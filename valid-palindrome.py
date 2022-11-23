class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        x = len(s) - 1
        while i < x:
            while i < x and not s[i].isalnum():
                i +=1
            while i < x and not s[x].isalnum():
                x -=1   
            if(s[i].lower() != s[x].lower()):
                return False
            print(s[i].lower(), s[x].lower())    
            i += 1
            x -= 1
        return True
        

#       string = "".join([i for i in s if i.isalpha()])
#       x = len(string) - 1
#       i = 0
#         for i in string:
#             if(string.index(i) == x and len(s) == 1):
#                 return True
            
#             if(i.lower() != string[x].lower()):
#                 return False
            
#             x -=1
#             print(i, string[x])
