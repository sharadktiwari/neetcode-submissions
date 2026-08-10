class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)-1):
        #     diff = target - nums[i]
        #     for j in range(i+1, len(nums)):
        #         if diff == nums[j]:
        #             return [i, j]

        diff_dict = {v:i for i,v in enumerate(nums) }

        for i,v in enumerate(nums):
            diff = target-v
            if diff in diff_dict and diff_dict[diff] != i:
                return [i, diff_dict[diff]]