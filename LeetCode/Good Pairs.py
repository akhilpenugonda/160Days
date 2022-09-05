from ast import List


class Solution:
    def numIdenticalPairsIter(self, nums: List[int]) -> int:
        response = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] == nums[j]):
                    response += 1
        return response
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dp = [0 for i in range(101)]
        count = 0
        for i in range(len(nums)):
            count += dp[nums[i]]
            dp[nums[i]] += 1
        return count