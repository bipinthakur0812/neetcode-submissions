class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_index = 0
        
        for read_index in range(len(nums)):
            # If the current element is NOT the value we want to delete
            if nums[read_index] != val:
                # Copy it forward to the write position
                nums[write_index] = nums[read_index]
                write_index += 1
                
        # write_index naturally tracks the total count of valid elements
        return write_index
        