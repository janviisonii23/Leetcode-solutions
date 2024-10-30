class Solution:
    def twoEggDrop(self, n: int) -> int:
        for i in range(n + 1):
            if int((i * (i + 1)) / 2) >= n:
                return i

        return 0
