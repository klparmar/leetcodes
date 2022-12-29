# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        foundAddy = set()
        temp = head

        while temp:
            if id(temp) in foundAddy:
                return True
            else:
                foundAddy.add(id(temp))
            temp = temp.next
            
        return False
