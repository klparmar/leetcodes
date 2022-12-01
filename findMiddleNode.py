# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #go thru list first get # of nodes
        x = head
        cnt = 0
        while x != None:
            cnt +=1
            x = x.next
        
        #if nodes are even make our y = the second middle #
        x = head
        if cnt % 2 == 0:
            y = (cnt /2 ) + 1
        else:   #else divide number of nodes by 2 and ciel
            y = ceil(cnt /2)
        cnt = 0
        
        #loop thru list until we reach yth node
        while cnt < y - 1:
            cnt +=1
            x = x.next

        return x
    
    #O(n) time 
    
#Runtime: 59 ms, faster than 40.35% of Python3 online submissions for Middle of the Linked List.
#Memory Usage: 13.8 MB, less than 55.98% of Python3 online submissions for Middle of the Linked List.
        
