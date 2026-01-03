#1480. Running Sum of 1d Array
#leetcode username: shravani8_8

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        newnum = [] 
        newnum.append(nums[0]) 

        for i in range(1, n):
            val = newnum[i-1] + nums[i]
            newnum.append(val) 

        return newnum
    
        