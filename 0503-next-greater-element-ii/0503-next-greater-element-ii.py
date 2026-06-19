# Date: 2026.06.19
# Problem: 503. Next Greater Element II
#
# Approach: Monotonic Stack + Circular Array
#
# 각 원소에 대해 오른쪽 방향으로 처음 만나는 더 큰 값을 찾는 문제.
# 단, 배열이 원형이므로 끝까지 갔을 때 다시 처음부터 이어서 확인해야 한다.
#
# 일반적인 next greater element처럼,
# 아직 더 큰 값을 찾지 못한 index들을 stack에 저장한다.
#
# 1차 순회:
# - 일반 배열처럼 오른쪽에 있는 더 큰 값을 찾는다.
# - 현재 값이 stack top의 값보다 크면,
#   stack top index의 next greater를 현재 값으로 확정한다.
#
# 2차 순회:
# - 원형 배열 조건을 처리하기 위해 nums를 한 번 더 앞에서부터 확인한다.
# - 이때는 새로운 index를 stack에 추가하지 않고,
#   1차 순회에서 아직 답을 찾지 못한 index들만 해결한다.
#
# stack에는 값이 아니라 index를 저장한다.
# answer의 초기값은 -1로 두고,
# 끝까지 더 큰 값을 찾지 못한 원소는 그대로 -1이 된다.
#
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [-1] * n
        stack = []

        for i in range(2 * n):
            idx = i % n

            while stack and nums[stack[-1]] < nums[idx]:
                prev_idx = stack.pop()
                answer[prev_idx] = nums[idx]

            if i < n:
                stack.append(idx)

        return answer