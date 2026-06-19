# Date: 2026.06.19
# Problem: 739. Daily Temperatures
#
# Approach: Monotonic Stack
#
# 각 날짜마다 이후에 더 따뜻한 날이 몇 일 뒤에 오는지 구하는 문제.
# 매번 오른쪽을 전부 탐색하면 O(N^2)이 되므로,
# 아직 더 따뜻한 날을 찾지 못한 index들을 stack에 저장한다.
#
# stack은 온도가 내림차순이 되도록 유지한다.
# 현재 온도가 stack top의 온도보다 높다면,
# stack top 날짜는 현재 날짜를 통해 정답을 확정할 수 있다.
#
# answer[prev_idx] = current_idx - prev_idx
#
# 같은 온도는 더 따뜻한 날이 아니므로 비교는 < 로 한다.
#
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [(temperatures[0], 0)]

        for i in range(1, len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                temperature, idx = stack.pop()
                answer[idx] = i - idx

            stack.append((temperatures[i], i))

        return answer


        