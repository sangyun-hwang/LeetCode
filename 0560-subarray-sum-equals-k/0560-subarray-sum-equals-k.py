# Date: 2026.06.18
# Problem: 560. Subarray Sum Equals K
#
# Approach: Prefix Sum + HashMap
#
# 문제 핵심:
# - nums 안에서 합이 k가 되는 "연속 부분 배열(subarray)"의 개수를 구해야 한다.
# - subarray는 중간 원소를 건너뛸 수 없고, 시작점과 끝점을 정해서 자른 연속 구간이다.
#
#
# 1. 처음 생각한 접근: k보다 큰 값 제외
# - 처음에는 목표값 k보다 큰 수가 있는 index를 제외하면 탐색 범위를 줄일 수 있다고 생각했다.
# - 하지만 nums에는 음수가 포함될 수 있다.
#
# 예:
# nums = [10, -7, 2], k = 5
# 10 + (-7) + 2 = 5
#
# - k보다 큰 값이 있어도 음수와 합쳐져 정답 구간이 될 수 있으므로 이 방법은 사용할 수 없다.
#
#
# 2. Sliding Window 접근 검토
# - 연속 구간 문제이므로 left, right를 움직이는 Sliding Window를 생각했다.
# - 하지만 음수가 있으면 right를 늘렸을 때 합이 항상 커지지 않고,
#   left를 줄였을 때 합이 항상 작아지지도 않는다.
#
# - 따라서 다음과 같은 판단이 불가능하다.
#   - 현재 합이 k보다 크면 left를 옮긴다.
#   - 현재 합이 k보다 작으면 right를 늘린다.
#
# - 이 문제에서는 nums에 음수가 포함될 수 있으므로 Sliding Window는 적합하지 않다.
#
#
# 3. 음수/양수 구간 분리 또는 압축 접근 검토
# - 음수를 제외한 연속 구간을 먼저 계산하거나,
#   음수를 포함한 구간 중 합이 양수가 되는 경우를 압축해서 다시 계산하는 방식도 생각했다.
# - 하지만 이 문제는 원래 배열에서 만들어지는 모든 연속 구간의 개수를 세는 문제다.
# - 구간을 임의로 나누거나 압축하면 서로 다른 subarray의 개수 정보가 사라질 수 있다.
#
# 예:
# nums = [1, -1, 1], k = 1
#
# 정답 구간:
# [1]          # index 0
# [1, -1, 1]  # index 0 ~ 2
# [1]          # index 2
#
# - 따라서 부호 기준으로 구간을 나누는 방식은 문제 조건과 맞지 않는다.
#
#
# 4. Prefix Sum 접근
# - 연속 구간 합은 누적합의 차이로 표현할 수 있다.
#
# sum(i ~ j) = prefix[j + 1] - prefix[i]
#
# - prefix sum을 미리 만들어두면 각 구간 합은 O(1)에 구할 수 있다.
# - 하지만 모든 i, j 조합을 확인하면 전체 연속 구간 개수는 O(N^2)이므로 시간 초과 가능성이 높다.
#
#
# 5. Prefix Sum + HashMap으로 개선
# - 현재까지의 누적합을 curr라고 하자.
# - 어떤 이전 누적합 prev가 있었을 때, prev 이후부터 현재 위치까지의 구간 합은:
#
# curr - prev
#
# - 이 값이 k가 되려면:
#
# curr - prev = k
# prev = curr - k
#
# - 즉 현재 위치에서 끝나는 정답 구간의 개수는,
#   이전에 나온 누적합 중 curr - k가 몇 번 있었는지와 같다.
#
#
# 6. HashMap에 저장하는 값
# - prefix_count는 지금까지 등장한 누적합의 개수를 저장한다.
#
# prefix_count[prefix_sum] = 해당 누적합이 등장한 횟수
#
# - 현재 누적합 curr에 대해:
#
# need = curr - k
# answer += prefix_count[need]
#
# - 그 다음 현재 curr을 prefix_count에 추가한다.
#
#
# 7. 순서 주의
# - 현재 curr을 먼저 저장하면 안 된다.
# - 먼저 need = curr - k가 이전에 몇 번 나왔는지 확인한 뒤,
#   현재 curr을 저장해야 한다.
#
# 이유:
# - 현재 prefix를 먼저 저장하면 k = 0 같은 경우 길이 0짜리 구간을 잘못 셀 수 있다.
#
#
# 8. 초기값 prefix_count[0] = 1
# - 아무 원소도 선택하지 않았을 때의 누적합 0을 미리 1번 등장한 것으로 처리한다.
# - 그래야 배열의 시작부터 현재 위치까지의 합이 k인 경우를 잡을 수 있다.
#
# 예:
# nums = [1, 2], k = 3
#
# curr = 3일 때
# need = curr - k = 0
#
# prefix_count[0]이 있어야 [1, 2] 구간을 정답으로 셀 수 있다.
#
#
# 9. 전체 흐름
# - prefix_count = {0: 1}로 시작한다.
# - curr = 0, answer = 0으로 시작한다.
# - nums를 왼쪽부터 순회하면서 curr에 현재 값을 더한다.
# - need = curr - k를 구한다.
# - 이전에 need가 등장한 횟수만큼 answer에 더한다.
# - 현재 curr을 prefix_count에 기록한다.
#
#
# Complexity:
# - Time Complexity: O(N)
# - Space Complexity: O(N)


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        prefix_count = {0: 1}
        curr = 0

        for num in nums:
            curr += num

            need = curr - k

            answer += prefix_count.get(need, 0)

            prefix_count[curr] = prefix_count.get(curr, 0) + 1

        return answer