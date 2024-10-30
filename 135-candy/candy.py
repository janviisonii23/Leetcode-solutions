class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        l = [0]*n
        l[0]=1
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                l[i] = l[i-1]+1
            else:
                l[i]=1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                l[i] = max(l[i], l[i + 1] + 1)
        return sum(l)
