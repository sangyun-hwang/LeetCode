# Date: 2026.06.28
# Problem: 34. Find First and Last Position of Element in Sorted Array
#
# Approach: Binary Search / Boundary Search
#
# 정렬된 배열에서 target이 처음 등장하는 위치와
# 마지막으로 등장하는 위치를 찾는 문제.
# target이 존재하지 않으면 [-1, -1]을 반환한다.
#
# 단순히 target 하나를 찾는 일반 이분탐색으로는 부족하다.
# nums[mid] == target인 값을 찾더라도,
# 그 위치가 첫 번째 target인지 마지막 target인지 알 수 없기 때문이다.
#
# 따라서 이분탐색을 두 번 수행한다.
#
# 1. find_left():
# - target의 가장 왼쪽 위치를 찾는다.
# - nums[mid] == target이면 answer에 mid를 저장한다.
# - 하지만 더 왼쪽에도 target이 있을 수 있으므로 right = mid - 1로 이동한다.
# - nums[mid] >= target이면 왼쪽 경계를 더 확인해야 하므로 right를 줄인다.
# - nums[mid] < target이면 target은 오른쪽에 있으므로 left를 키운다.
#
# 2. find_right():
# - target의 가장 오른쪽 위치를 찾는다.
# - nums[mid] == target이면 answer에 mid를 저장한다.
# - 하지만 더 오른쪽에도 target이 있을 수 있으므로 left = mid + 1로 이동한다.
# - nums[mid] <= target이면 오른쪽 경계를 더 확인해야 하므로 left를 키운다.
# - nums[mid] > target이면 target은 왼쪽에 있으므로 right를 줄인다.
#
# 핵심 아이디어:
# - target을 발견해도 바로 종료하지 않는다.
# - answer에 후보 위치를 저장한 뒤,
#   왼쪽 경계 또는 오른쪽 경계를 끝까지 탐색한다.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left() -> int:
            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= target:
                    if nums[mid] == target:
                        answer = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return answer

        def find_right() -> int:
            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] <= target:
                    if nums[mid] == target:
                        answer = mid
                    left = mid + 1
                else:
                    right = mid - 1

            return answer

        return [find_left(), find_right()]




        