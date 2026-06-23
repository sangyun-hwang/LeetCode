# Date: 2026.06.23
# Problem: 1482. Minimum Number of Days to Make m Bouquets
#
# Approach: Binary Search on Answer
#
# m개의 꽃다발을 만들 수 있는 최소 날짜를 구하는 문제.
# 꽃다발 1개를 만들기 위해서는 연속된 k개의 핀 꽃이 필요하다.
#
# 날짜 day가 커질수록 피어난 꽃의 개수는 늘어나므로,
# 어떤 day에 꽃다발을 만들 수 있다면 그 이후 날짜도 모두 가능하다.
# 따라서 가능/불가능이 한쪽으로 나뉘는 구조이므로 이분탐색을 사용할 수 있다.
#
# Search Range:
# - left = min(bloomDay)
#   가장 빠르게 꽃이 피는 날짜
#
# - right = max(bloomDay)
#   모든 꽃이 피는 날짜
#
# 불가능 조건:
# - 필요한 꽃의 총 개수는 m * k개이다.
# - m * k > len(bloomDay)이면 어떤 날짜가 와도 꽃다발을 만들 수 없으므로 -1을 반환한다.
#
# can(day):
# - bloomDay를 왼쪽부터 순회한다.
# - bloom <= day 이면 해당 꽃은 피어 있으므로 연속 count를 증가시킨다.
# - count == k가 되면 꽃다발 1개를 만들고, 사용한 꽃은 다시 쓸 수 없으므로 count를 0으로 초기화한다.
# - bloom > day 이면 아직 안 핀 꽃이므로 연속 구간이 끊기고 count를 0으로 초기화한다.
# - bouquet >= m 이 되면 해당 day는 가능한 날짜이다.
#
# can(mid) == True:
# - mid일에는 꽃다발을 만들 수 있다.
# - 더 빠른 날짜도 가능한지 확인해야 하므로 right를 줄인다.
#
# can(mid) == False:
# - mid일에는 꽃이 부족하다.
# - 더 늦은 날짜가 필요하므로 left를 키운다.

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def can(day: int) -> bool:
            bouquet = 0
            count = 0

            for bloom in bloomDay:
                if bloom <= day:
                    count += 1

                    if count == k:
                        bouquet += 1
                        count = 0

                        if bouquet >= m:
                            return True
                else:
                    count = 0

            return False

        if m * k > len(bloomDay):
            return -1

        left = min(bloomDay)
        right = max(bloomDay)
        answer = right

        while left <= right:
            mid = (left + right) // 2

            if can(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer

        