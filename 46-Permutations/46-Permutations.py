class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            permutations = self.permute(nums)

            for i in permutations:
                i.append(n)
            res.extend(permutations)
            nums.append(n)

        return res

