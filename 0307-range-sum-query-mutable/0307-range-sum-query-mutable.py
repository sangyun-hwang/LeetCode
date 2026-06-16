## 2026.06.16

# - Problem: 307. Range Sum Query - Mutable
# - Topic: Fenwick Tree / Segment Tree
# - Reason: 동적 업데이트 + 구간 조회 연습. 코테 4번 장애물 구간 체크 문제와 연결됨.
# - Goal: Fenwick Tree의 update / prefix_sum / range_sum 구조 익히기

# 1. Brute Force
# - nums 배열을 그대로 저장한다.
# - update는 nums[index]만 바꾸면 되므로 O(1)
# - sumRange는 left부터 right까지 직접 순회하며 더하므로 O(N)
#
# Constraints:
# - nums.length <= 3 * 10^4
# - update / sumRange 호출 횟수 <= 3 * 10^4
#
# 최악의 경우 sumRange가 매번 긴 구간을 조회하면
# O(N * Q) = 3 * 10^4 * 3 * 10^4 = 9 * 10^8 수준의 연산이 발생할 수 있다.
# 따라서 Brute Force는 시간 초과가 발생한다.
#
# Brute Force 풀이 기록:
#
# class NumArray:
#
#     def __init__(self, nums: List[int]):
#         self.n = len(nums)
#         self.nums = nums[:]
#
#     def update(self, index: int, val: int) -> None:
#         self.nums[index] = val
#
#     def sumRange(self, left: int, right: int) -> int:
#         total = 0
#
#         for i in range(left, right + 1):
#             total += self.nums[i]
#
#         return total
#
#
# 2. Prefix Sum
# - prefix[i]를 nums[0] ~ nums[i - 1]까지의 합으로 저장한다.
# - sumRange(left, right)는 prefix[right + 1] - prefix[left]로 O(1)에 계산할 수 있다.
#
# 하지만 update(index, val)가 발생하면 nums[index] 값이 바뀌므로,
# index 이후의 prefix 값들을 모두 수정해야 한다.
#
# - update: O(N)
# - sumRange: O(1)
#
# 이 문제는 update도 많이 호출될 수 있으므로 Prefix Sum도 최악의 경우 시간 초과가 발생한다.
#
# Prefix Sum 풀이 기록:
#
# class NumArray:
#
#     def __init__(self, nums: List[int]):
#         self.n = len(nums)
#         self.nums = nums[:]
#         self.prefix = [0] * (self.n + 1)
#
#         for i in range(self.n):
#             self.prefix[i + 1] = self.prefix[i] + self.nums[i]
#
#     def update(self, index: int, val: int) -> None:
#         diff = val - self.nums[index]
#         self.nums[index] = val
#
#         for i in range(index + 1, self.n + 1):
#             self.prefix[i] += diff
#
#     def sumRange(self, left: int, right: int) -> int:
#         return self.prefix[right + 1] - self.prefix[left]
#
#
# 3. Segment Tree
# - 각 노드가 특정 구간의 합을 저장하는 트리 구조
# - update 시 변경된 index를 포함하는 경로만 갱신
# - query 시 요청 구간과 겹치는 노드의 합만 사용
# - build: O(N), update: O(log N), sumRange: O(log N)
#
# Segment Tree로도 통과 가능하지만,
# 재귀 기반 구현이라 코드가 비교적 길고 Python에서는 실행 시간이 아슬아슬할 수 있다.
#
# Segment Tree 풀이 기록:
#
# class NumArray:
#
#     def __init__(self, nums: List[int]):
#         self.n = len(nums)
#         self.nums = nums[:]
#         self.tree = [0] * (4 * self.n)
#         self.build(1, 0, self.n - 1)
#
#     def build(self, node: int, start: int, end: int):
#         if start == end:
#             self.tree[node] = self.nums[start]
#             return self.tree[node]
#
#         mid = (start + end) // 2
#
#         left_sum = self.build(node * 2, start, mid)
#         right_sum = self.build(node * 2 + 1, mid + 1, end)
#
#         self.tree[node] = left_sum + right_sum
#
#         return self.tree[node]
#
#     def update_tree(self, node: int, start: int, end: int, index: int, val: int):
#         if start == end:
#             self.tree[node] = val
#             return
#
#         mid = (start + end) // 2
#
#         if index <= mid:
#             self.update_tree(node * 2, start, mid, index, val)
#         else:
#             self.update_tree(node * 2 + 1, mid + 1, end, index, val)
#
#         self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
#
#     def query(self, node: int, start: int, end: int, left: int, right: int) -> int:
#         if right < start or end < left:
#             return 0
#         elif left <= start and end <= right:
#             return self.tree[node]
#         else:
#             mid = (start + end) // 2
#
#             left_sum = self.query(node * 2, start, mid, left, right)
#             right_sum = self.query(node * 2 + 1, mid + 1, end, left, right)
#
#             return left_sum + right_sum
#
#     def update(self, index: int, val: int) -> None:
#         self.nums[index] = val
#         self.update_tree(1, 0, self.n - 1, index, val)
#
#     def sumRange(self, left: int, right: int) -> int:
#         return self.query(1, 0, self.n - 1, left, right)
#
#
# 4. Fenwick Tree / Binary Indexed Tree
# - Segment Tree보다 구현이 짧고, update와 prefix sum을 모두 O(log N)에 처리할 수 있다.
# - tree[i]는 i에서 끝나는 lowbit(i) 길이의 구간 합을 저장한다.
#
# 예:
# - tree[6]은 lowbit(6) = 2이므로 [5, 6] 구간 합을 저장
# - tree[12]는 lowbit(12) = 4이므로 [9, 12] 구간 합을 저장
#
# prefix_sum(index):
# - 현재 tree[index]가 담당하는 구간 합을 더한다.
# - 이후 index -= lowbit(index)로 그 구간을 제외한 왼쪽 prefix로 이동한다.
#
# update(index, diff):
# - index를 포함하는 Fenwick Tree 구간들에 diff를 반영한다.
# - 이후 index += lowbit(index)로 다음 영향을 받는 구간으로 이동한다.
#
# Complexity:
# - build: O(N log N)
# - update: O(log N)
# - sumRange: O(log N)


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]

        # Fenwick Tree는 1-index로 다룬다.
        # 따라서 0번 index는 사용하지 않고 n + 1 크기로 만든다.
        self.tree = [0] * (self.n + 1)

        # 초기 tree는 모든 값이 0인 상태다.
        # 각 nums[i]를 0에서 nums[i]로 변경한다고 생각하면,
        # diff = nums[i] - 0 = nums[i] 이므로 add(i + 1, nums[i])로 초기화할 수 있다.
        for i, num in enumerate(nums):
            self.add(i + 1, num)

    def lowbit(self, x: int) -> int:
        # x에서 가장 오른쪽에 있는 1의 자리값을 구한다.
        #
        # 예:
        # 12 = 1100
        # lowbit(12) = 4
        return x & -x

    def add(self, index: int, diff: int) -> None:
        # nums의 특정 위치 값이 diff만큼 변했을 때,
        # 그 위치를 포함하는 Fenwick Tree의 구간 합들에 diff를 반영한다.
        #
        # 이동 방향:
        # index -> index + lowbit(index)
        #
        # 예:
        # 5 -> 6 -> 8 -> 16 ...
        while index <= self.n:
            self.tree[index] += diff
            index += self.lowbit(index)

    def prefix_sum(self, index: int) -> int:
        # 1번부터 index번까지의 누적합을 구한다.
        #
        # tree[index]가 담당하는 구간 합을 더한 뒤,
        # 그 구간을 제외한 왼쪽 prefix로 이동한다.
        #
        # 이동 방향:
        # index -> index - lowbit(index)
        #
        # 예:
        # 13 -> 12 -> 8 -> 0
        total = 0

        while index > 0:
            total += self.tree[index]
            index -= self.lowbit(index)

        return total

    def update(self, index: int, val: int) -> None:
        # LeetCode의 index는 0-index이고,
        # Fenwick Tree의 index는 1-index이다.
        #
        # Fenwick Tree에는 새 값을 직접 넣는 것이 아니라,
        # 기존 값과 새 값의 차이만큼만 반영한다.
        diff = val - self.nums[index]

        # 원본 배열도 최신 값으로 갱신해두어야
        # 다음 update에서 diff를 정확히 계산할 수 있다.
        self.nums[index] = val

        # Fenwick Tree에서는 index + 1 위치부터 diff를 반영한다.
        self.add(index + 1, diff)

    def sumRange(self, left: int, right: int) -> int:
        # sumRange(left, right)
        # = nums[left] ~ nums[right]의 합
        #
        # prefix_sum(right) - prefix_sum(left - 1) 형태로 계산한다.
        #
        # 다만 LeetCode는 0-index이고 Fenwick Tree는 1-index이므로:
        # - right는 right + 1까지 포함
        # - left 이전 구간은 left까지의 prefix_sum으로 표현된다.
        return self.prefix_sum(right + 1) - self.prefix_sum(left)

