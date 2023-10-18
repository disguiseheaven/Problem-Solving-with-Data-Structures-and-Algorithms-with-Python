#Missing number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
         originalsum = int(len(nums)*(len(nums)+1)/2)
         presentsum = sum(nums)
         return(originalsum-presentsum)  
        
