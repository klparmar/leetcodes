class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        biggest = -1
        
        for i in reversed(range(len(arr))):
            temp = arr[i]
            arr[i] = biggest

            if temp >= biggest:
                biggest = temp

        return arr
        
