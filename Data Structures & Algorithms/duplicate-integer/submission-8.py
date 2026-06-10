class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #seen = set()
        #for num in nums:
        #    if num in seen:
        #        return True
        #    seen.add(num)
        #return False
        nums.sort()  # Sorts the list in-place (uses O(1) extra memory in Python)
        
        # Check if any neighboring elements are the same
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
                
        return False
        