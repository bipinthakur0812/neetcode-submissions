class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        occ = {}
        n = len(nums)
        for i in nums:
            occ[i] = occ.get(i,0) + 1
            if occ[i] >= n/2:
                return i

        