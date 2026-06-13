class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            answer = max(answer, current)
        
        return answer