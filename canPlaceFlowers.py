class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = -1
        cnt = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                prev = flowerbed[i]
            elif flowerbed[i] == 0:
                if prev != 1:
                    if i == len(flowerbed) - 1 or flowerbed[i + 1] != 1:
                        cnt += 1
                        prev = 1
                else:
                    prev = 0

        return cnt >= n
