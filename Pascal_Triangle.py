class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        
        arr = []
        
        
        i = 0
        x = 0
        subArr = []
        
        # length of our array is 0 keep looping until we have numRows amount of rows
        while len(arr) < numRows:
            while i < len(arr):         #generate the subarray for each index of arr
                if i == 0:              #add 1 to first index
                    subArr.append(1)
                else:                   #else, add adjacent values from prev subarray to index
                    subArr.append(arr[len(arr) - 1][i] + arr[len(arr) - 1][x])
                    x +=1
                i +=1
                
            #last index of subarray is always 1 so add that to last index    
            subArr.append(1)
            
            #add subarray to our array
            arr.append(subArr)
            
            #reset values for next iteration
            i = 0
            x = 0
            subArr = []
            
        return arr
