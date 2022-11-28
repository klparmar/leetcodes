/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
        ListNode x = list1;
        ListNode y = list2;
        
        //if lists are null return
        if(x == null && y == null)
            return null;
        //construct new list that we will build and return and pointer z
        ListNode newList = new ListNode();
        ListNode z = newList;
        
        
        //go through the lists until we reach end of both
        while( x != null || y!=null){
            if(y == null){    //if we already finished list2 just add list1 element
                z.val = x.val;
                x = x.next;
            }else if(x == null){  //if we finished list1 just add list2 element
                z.val = y.val;
                y = y.next;
            }else if(x.val <= y.val){ //if neither are null, add from list1 if the value is less than or equal to list2 val
                z.val = x.val;
                x = x.next; 
            }else{  //else means y.val < x.val so add y value
                z.val = y.val;
                y = y.next;
            }

            if(!(x == null && y == null)) //create next node of our newList
                z.next = new ListNode();
            z = z.next;
            
        }
        
        return newList;
    }
}

//Runtime: 0 ms, faster than 100.00% of Java online submissions for Merge Two Sorted Lists.
//Memory Usage: 41.7 MB, less than 93.14% of Java online submissions for Merge Two Sorted Lists.
