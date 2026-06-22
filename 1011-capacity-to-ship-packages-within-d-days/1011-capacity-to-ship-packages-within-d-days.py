# Date: 2026.06.22
# Problem: 1011. Capacity To Ship Packages Within D Days
#
# Approach: Binary Search on Answer
#
# days일 안에 모든 package를 순서대로 배송할 수 있는
# 최소 배 용량 capacity를 구하는 문제.
#
# 배열 index를 이분탐색하는 것이 아니라,
# 가능한 정답값인 capacity를 이분탐색한다.
#
# capacity가 작으면 필요한 배송 일수가 많아지고,
# capacity가 크면 필요한 배송 일수가 줄어든다.
#
# 따라서 어떤 capacity로 days일 안에 배송할 수 있다면,
# 그보다 큰 capacity도 모두 가능하다.
# 이처럼 가능/불가능이 한쪽으로 나뉘므로 이분탐색을 사용할 수 있다.
#
# Search Range:
# - left = max(weights)
#   가장 무거운 package 하나는 반드시 실을 수 있어야 하므로
#   최소 capacity는 max(weights) 이상이어야 한다.
#
# - right = sum(weights)
#   모든 package를 하루에 전부 실으면 무조건 가능하므로
#   최대 capacity 후보는 sum(weights)이다.
#
# capacity 판별 방법:
# - weights를 순서대로 순회한다.
# - 현재 날짜에 weight를 더했을 때 capacity를 넘지 않으면 그대로 싣는다.
# - capacity를 넘으면 다음 날로 넘기고, current를 해당 weight로 초기화한다.
# - 필요한 day가 days 이하이면 가능한 capacity다.
#
# day <= days:
# - 현재 capacity는 가능하다.
# - 더 작은 capacity도 가능한지 확인해야 하므로 right를 줄인다.
#
# day > days:
# - 현재 capacity는 너무 작다.
# - 더 큰 capacity가 필요하므로 left를 키운다.

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        answer = right

        while left <= right:
            capacity = (left + right) // 2

            day = 1
            current = 0

            for weight in weights:
                if current + weight > capacity:
                    day += 1
                    current = weight
                else:
                    current += weight
            
            if day <= days:
                answer = capacity
                right = capacity - 1
            else:
                left = capacity + 1
        
        return answer
            

                

        