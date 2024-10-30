class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        res=-1
        nums=set(nums)
        
        for x in nums:
            if x**2  in nums:
                i=x
                c=1
                while(i**2 in nums):
                    c+=1
                    i=i**2

                res=max(res,c)
                # if res==5:break
        return res