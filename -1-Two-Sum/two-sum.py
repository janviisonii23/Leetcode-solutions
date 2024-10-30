class Solution:
    def twoSum(self, nums, target: int):
        visited = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in visited:
                return [visited[difference], i]
            else:
                visited[nums[i]] = i
