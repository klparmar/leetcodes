class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        stack2 = []
        
        for x in s:
            if x == '#' and len(stack) != 0:
                stack.pop()
            elif x !='#':
                stack.append(x)
        
        for x in t:
            if x == '#' and len(stack2) != 0:
                stack2.pop()
            elif x !='#':
                stack2.append(x) 
        
        return stack2 == stack
