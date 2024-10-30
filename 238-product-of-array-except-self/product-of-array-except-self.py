class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[1]*n
        right=[1]*n
        # left[0]=1
        # right[n-1]=1

        for i in range(1,n):
            left[i]=nums[i-1]*left[i-1]
        # print(left)
        for i in range(n-2,-1,-1):
            right[i]=nums[i+1]*right[i+1]
        res=[0]*n
        for i in range(n):
            res[i]=left[i]*right[i]
        return res

        
        