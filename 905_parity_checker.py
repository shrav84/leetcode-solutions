#905. Sort Array By Parity 
#leetcode username: shravani8_8 
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]: 
        n = len(nums)
        checker = 0
        for i in range(n):
            if nums[i]%2==0:
                temp = nums[i]
                nums[i] = nums[checker]
                nums[checker] = temp
                checker+=1 
        return nums 
                
        
