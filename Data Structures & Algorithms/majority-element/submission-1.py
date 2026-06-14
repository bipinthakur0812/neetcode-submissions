class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            # 1. If our current candidate runs out of votes, 
            #    the next number takes over as the new candidate.
            if count == 0:
                candidate = num
            
            # 2. If we see the same candidate, they gain a vote (+1).
            #    If we see an opponent, they lose a vote (-1).
            count += (1 if num == candidate else -1)
            
        return candidate

        