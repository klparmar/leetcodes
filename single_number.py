class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #create helper frequency dict
        x = {}
        #loop thru array, populate freq array 
        for i in nums:
            if x.get(i) == None:
                x[i] = 1          #add 1 for a number we have not seen
            else:
                x[i] +=1          #increment if we see repeat number
        
        #loop thru freq dict, any number that has value 1 return it
        #as it only appeared once in array so it is our single number
        for i in x:
            if x[i] == 1:
                return i
