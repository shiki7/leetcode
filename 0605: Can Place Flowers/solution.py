class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total = 0
        N = len(flowerbed)
        if N == 1:
            if flowerbed[0] == 0:
                total +=1
        else:
            for i in range(0, N):
                if flowerbed[i] == 0:
                    if (i == 0 and flowerbed[1] == 0) or (i == N-1 and flowerbed[i-1] == 0) or (i > 0 and i < N-1 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                        total += 1
                        flowerbed[i] = 1
        if n <= total:
            return True
        else:
            return False
