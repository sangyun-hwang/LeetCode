# Date: 2026.06.21
# Problem: 875. Koko Eating Bananas
#
# Approach: Binary Search on Answer
#
# h시간 안에 모든 바나나를 먹을 수 있는 최소 속도 k를 구하는 문제.
# 배열의 index를 이분탐색하는 것이 아니라,
# 가능한 정답값인 먹는 속도 k를 이분탐색한다.
#
# k가 작으면 먹는 데 걸리는 시간이 길어지고,
# k가 크면 먹는 데 걸리는 시간이 짧아진다.
#
# 따라서 어떤 k로 h시간 안에 먹을 수 있다면,
# 그보다 큰 k도 모두 가능하다.
# 이처럼 가능/불가능이 한쪽으로 나뉘므로 이분탐색을 사용할 수 있다.
#
# 각 pile을 먹는 데 걸리는 시간:
# - pile / k 를 올림한 값
# - Python에서는 (pile + k - 1) // k 로 계산할 수 있다.
#
# total_time <= h:
# - 현재 k는 가능한 속도
# - 더 작은 k도 가능한지 확인해야 하므로 right를 줄인다.
#
# total_time > h:
# - 현재 k는 너무 느림
# - 더 큰 k가 필요하므로 left를 키운다.
#
# Search Range:
# - 최소 속도: 1
# - 최대 속도: max(piles)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        answer = right

        while left <= right:
            k = (left + right) // 2

            total_time = sum((pile + k - 1) // k for pile in piles)

            if total_time <= h:
                answer = k
                right = k - 1
            else:
                left = k + 1

        return answer

        