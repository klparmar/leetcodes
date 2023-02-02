class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dictt = {}

        for i in wall:
            brickCount = 0
            for j in range(len(i) - 1):
                brickCount += i[j]
                if brickCount not in dictt:
                    dictt[brickCount] = 1
                else:
                    dictt[brickCount] += 1
        
        maxx = 0
        lowest = 0
        for i in dictt:
            maxx = max(maxx, dictt[i])
        return len(wall) - maxx
