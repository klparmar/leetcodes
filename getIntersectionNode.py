# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        temp1 = headA
        temp2 = headB
        foundAddys = set()
        while temp1 or temp2:
            if temp1:
                if id(temp1) in foundAddys:
                    return temp1
                else:
                    foundAddys.add(id(temp1))
                temp1 = temp1.next
            if temp2:
                if id(temp2) in foundAddys:
                    return temp2
                else:
                    foundAddys.add(id(temp2))
                temp2 = temp2.next

        return None
