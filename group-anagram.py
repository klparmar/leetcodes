class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictt = {}
        
        dict2 = collections.defaultdict(list)
        
        for i in strs:
            arr = [0] * 26
            for x in i:
                arr[ord(x) - ord("a")] += 1
                    
            dict2[tuple(arr)].append(i)
        
        soln = []
        for i in dict2:
            soln.append(dict2[i])
            
        return soln
