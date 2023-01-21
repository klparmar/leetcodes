class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if (stone1 - stone2) != 0:
                heapq.heappush(stones, stone1 - stone2)
            
            
        if stones == []:
            return 0

        return (stones[0] * -1)
