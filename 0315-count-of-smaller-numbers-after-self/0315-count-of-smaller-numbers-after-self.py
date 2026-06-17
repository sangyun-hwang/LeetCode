# Date: 2026.06.17
# Problem: 315. Count of Smaller Numbers After Self
#
# Approach: Coordinate Compression + Fenwick Tree
#
# 문제 핵심:
# - 각 nums[i]에 대해, 오른쪽에 있는 값들 중 nums[i]보다 작은 값의 개수를 구해야 한다.
#
#
# 1. Brute Force 접근
# - 각 index마다 오른쪽 원소를 전부 순회하면서 nums[i]보다 작은 값의 개수를 센다.
# - 로직은 직관적이지만, 매 원소마다 오른쪽 배열을 다시 확인해야 한다.
#
# Time Complexity:
# - O(N^2)
#
# 문제 크기가 커지면 시간 초과가 발생할 수 있다.
#
#
# 2. 관점 전환
# - 왼쪽에서 오른쪽으로 보면, 현재 원소의 오른쪽 값들을 매번 새로 확인해야 한다.
# - 반대로 오른쪽에서 왼쪽으로 순회하면,
#   지금까지 본 값들이 곧 현재 원소의 "오른쪽에 있는 값들"이 된다.
#
# 예:
# nums = [5, 2, 6, 1]
#
# 오른쪽부터 순회:
# - 1을 볼 때: 오른쪽에 본 값 없음
# - 6을 볼 때: 오른쪽에 [1]이 있음
# - 2를 볼 때: 오른쪽에 [6, 1]이 있음
# - 5를 볼 때: 오른쪽에 [2, 6, 1]이 있음
#
# 따라서 매 단계에서 필요한 것은:
# - 이미 본 값들 중 현재 값보다 작은 값의 개수
# - 현재 값을 "봤다"고 기록하는 것
#
#
# 3. Count 배열 아이디어
# - 값별 등장 횟수를 저장하면, 현재 값보다 작은 값들이 몇 번 등장했는지 셀 수 있다.
# - 하지만 nums 값은 음수일 수 있고 값의 범위가 클 수 있으므로,
#   값을 배열 index로 바로 사용하기 어렵다.
#
#
# 4. 좌표 압축
# - 값의 크기 순서는 유지하면서, 각 값을 1부터 시작하는 작은 index로 변환한다.
#
# 예:
# nums = [5, 2, 6, 1]
# sorted unique nums = [1, 2, 5, 6]
#
# rank:
# 1 -> 1
# 2 -> 2
# 5 -> 3
# 6 -> 4
#
# 이렇게 하면 값 자체가 아니라 rank를 Fenwick Tree의 index로 사용할 수 있다.
#
#
# 5. Fenwick Tree 사용
# - Fenwick Tree에는 원본 nums의 합을 저장하는 것이 아니라,
#   "오른쪽에서 이미 본 값들의 등장 횟수"를 저장한다.
#
# 현재 num의 압축 index를 idx라고 하면:
#
# - num보다 작은 값의 개수:
#   prefix_sum(idx - 1)
#
# - 현재 num을 봤다고 기록:
#   add(idx, 1)
#
# idx - 1을 조회하는 이유:
# - 문제는 "smaller"를 묻기 때문에 현재 값과 같은 값은 포함하면 안 된다.
# - 따라서 현재 값의 rank보다 작은 rank들만 조회한다.
#
#
# 6. 전체 흐름
# - nums의 unique 값을 정렬해서 좌표 압축 rank를 만든다.
# - nums를 오른쪽에서 왼쪽으로 순회한다.
# - 현재 값의 rank를 구한다.
# - prefix_sum(rank - 1)로 현재 값보다 작은 오른쪽 값의 개수를 구한다.
# - add(rank, 1)로 현재 값을 Fenwick Tree에 추가한다.
# - 오른쪽부터 답을 만들었으므로 마지막에 reverse한다.

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(set(nums))
        rank = {}

        for i, num in enumerate(sorted_nums):
            rank[num] = i + 1

        m = len(sorted_nums)
        tree = [0] * (m + 1)
        answer = []

        def prefix_sum(index: int) -> int:
            total = 0

            while index > 0:
                total += tree[index]
                index -= index & -index

            return total

        def add(index: int, value: int) -> None:
            while index <= m:
                tree[index] += value
                index += index & -index

        for num in reversed(nums):
            idx = rank[num]

            smaller_count = prefix_sum(idx - 1)
            answer.append(smaller_count)

            add(idx, 1)

        answer.reverse()
        return answer