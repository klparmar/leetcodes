class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        dictt = {")" : "(", "}" : "{", "]" : "["}
        
        for i in s:
            if i not in dictt:
                stack.append(i)
            else:
                if len(stack) !=0 and dictt[i] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
