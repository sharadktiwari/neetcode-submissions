class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod, zc = 1, 0

        for num in nums:
            if not num:
                zc+=1
                continue
            prod *= num

        out = [0] * n
        if zc > 1: return out

        for i, v in enumerate(nums):
            if zc:
                if v:
                    out[i] = 0
                else:
                    out[i] = prod
            else:
                out[i] = prod//v
        return out
