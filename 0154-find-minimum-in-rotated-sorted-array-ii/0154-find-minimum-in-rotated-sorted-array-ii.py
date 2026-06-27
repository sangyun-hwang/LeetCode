# Date: 2026.06.27
# Problem: 154. Find Minimum in Rotated Sorted Array II
#
# Approach: Binary Search
#
# 정렬된 배열이 회전되어 있을 때 최솟값을 찾는 문제.
# 153번과 달리 nums에 중복값이 존재할 수 있다.
#
# 중복이 없다면 nums[mid]와 nums[right]를 비교해서
# 최솟값이 어느 쪽에 있는지 항상 판단할 수 있다.
#
# 하지만 중복이 있는 경우 nums[mid] == nums[right]가 될 수 있고,
# 이때는 최솟값이 왼쪽에 있는지 오른쪽에 있는지 확실히 판단할 수 없다.
# 따라서 이 경우에는 right를 1 줄여 탐색 범위를 좁힌다.
#
# 핵심 아이디어:
# - 최솟값 후보를 항상 [left, right] 범위 안에 남겨둔다.
# - left == right가 되면 해당 위치가 최솟값이다.
#
# nums[mid] > nums[right]:
# - mid가 왼쪽의 큰 값 구간에 있다는 뜻이다.
# - 최솟값은 mid 오른쪽에 있으므로 left = mid + 1로 이동한다.
#
# nums[mid] < nums[right]:
# - mid ~ right 구간은 정렬되어 있다.
# - 이 구간의 최솟값 후보는 nums[mid]이므로 right = mid로 이동한다.
# - mid도 최솟값일 수 있으므로 mid를 제외하지 않는다.
#
# nums[mid] == nums[right]:
# - 중복값 때문에 어느 쪽에 최솟값이 있는지 판단할 수 없다.
# - nums[right]와 같은 값이 mid에도 있으므로 right를 하나 줄여도
#   최솟값 후보를 잃지 않는다.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] == nums[right]:
                right -= 1
                continue

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]