class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) -1
        while (h >= l):
            m = (l + h)//2
            if(nums[m] == target):
                return m
            if(nums[m] > target):
                h = m - 1
            if(nums[m] < target):
                l = m + 1
        return -1