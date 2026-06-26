# Date: 2026.06.26
# Problem: 33. Search in Rotated Sorted Array
#
# Approach: Binary Search
#
# 정렬된 배열이 회전되어 있을 때,
# target의 index를 O(log N)에 찾는 문제.
# target이 없으면 -1을 반환한다.
#
# 회전된 정렬 배열에서는 전체 배열은 정렬되어 있지 않지만,
# mid를 기준으로 왼쪽 구간 또는 오른쪽 구간 중 하나는 반드시 정렬되어 있다.
#
# 핵심 아이디어:
# - nums[mid]가 target이면 바로 mid를 반환한다.
# - 그렇지 않으면 nums[left]와 nums[mid]를 비교해
#   왼쪽 구간이 정렬되어 있는지 확인한다.
#
# nums[left] <= nums[mid]:
# - left ~ mid 구간이 정렬되어 있다는 뜻이다.
# - target이 nums[left] <= target < nums[mid] 범위에 있으면
#   target은 왼쪽 구간에 있으므로 right = mid - 1로 이동한다.
# - 그렇지 않으면 오른쪽 구간을 탐색해야 하므로 left = mid + 1로 이동한다.
#
# nums[left] > nums[mid]:
# - mid ~ right 구간이 정렬되어 있다는 뜻이다.
# - target이 nums[mid] < target <= nums[right] 범위에 있으면
#   target은 오른쪽 구간에 있으므로 left = mid + 1로 이동한다.
# - 그렇지 않으면 왼쪽 구간을 탐색해야 하므로 right = mid - 1로 이동한다.
#
# 주의할 점:
# - 오른쪽 정렬 구간을 확인할 때는 nums[left]가 아니라 nums[right]와 비교해야 한다.
# - 탐색이 끝날 때까지 target을 찾지 못하면 -1을 반환한다.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid


            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                
        
        return -1
        