# Date: 2026.06.25
# Problem: 153. Find Minimum in Rotated Sorted Array
#
# Approach: Binary Search
#
# 정렬된 배열이 회전되어 있을 때 최솟값을 O(log N)에 찾는 문제.
# 단순히 전체를 순회하면 O(N)이므로, 배열의 정렬된 구조를 이용해 이분탐색한다.
#
# 핵심 아이디어:
# - nums[mid]와 nums[right]를 비교해서 최솟값이 어느 쪽에 있는지 판단한다.
#
# nums[mid] > nums[right]:
# - mid가 왼쪽의 큰 값 구간에 있다는 뜻이다.
# - 최솟값은 mid 오른쪽에 있으므로 left = mid + 1로 이동한다.
#
# nums[mid] <= nums[right]:
# - mid부터 right까지는 정렬된 구간이다.
# - 이 구간의 최솟값 후보는 nums[mid]이므로 answer를 갱신한다.
# - 더 왼쪽에 더 작은 값이 있을 수 있으므로 right = mid - 1로 이동한다.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]