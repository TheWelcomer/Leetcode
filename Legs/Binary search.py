class Solution:
    def search(self, nums: List[int], target: int) -> int:
        searchPos = len(nums)//2
        if target == nums[searchPos]:
            return searchPos
        elif target < nums[searchPos]:
            return self.search(nums[:searchPos], target)
        elif target > nums[searchPos]:
            return self.search(nums[searchPos:], target) + searchPos