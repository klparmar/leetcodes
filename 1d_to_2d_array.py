class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        #create helper stuff
        arr = []
        x = 0
        counter = 0
        arr2 = []
        
        #Loop thru og array
        for i in original:
          
            #have a counter to see many elements in arr[] if it equals m then not possible
            if x == m:
                return []
            
            #add element to subarray incr counter
            arr2.append(i)
            counter += 1
            
            #if we have n elements in subarray we need to start adding in next subarray
            if counter == n:
                arr.append(arr2)
                counter = 0
                arr2 = []
                x +=1
                
        #if after loop our counter of subarrays doesnt equal m then not possible
        if x != m:
                return []    
        return arr
        
        
# Runtime: 3033 ms, faster than 10.75% of Python3 online submissions for Convert 1D Array Into 2D Array.
# Memory Usage: 22.4 MB, less than 9.41% of Python3 online submissions for Convert 1D Array Into 2D Array.
