## 2026.06.16

# - Problem: 307. Range Sum Query - Mutable
# - Topic: Fenwick Tree / Segment Tree
# - Reason: 동적 업데이트 + 구간 조회 연습. 코테 4번 장애물 구간 체크 문제와 연결됨.
# - Goal: Fenwick Tree의 update / prefix_sum / range_sum 구조 익히기

class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]  
        
        # Fenwick Tree는 1-index로 다루기 때문에 n + 1 크기
        self.tree = [0] * (self.n + 1)

        # nums의 각 값을 Fenwick Tree에 반영
        # nums index는 0부터 시작하지만,
        # tree index는 1부터 시작하므로 i + 1로 넣기
        for i, num in enumerate(nums):
            self.add(i + 1, num)

    def lowbit(self, x: int) -> int:
        # x에서 가장 오른쪽 1의 자리값
        # 예: 12(1100) -> 4
        return x & -x

    def add(self, index: int, diff: int) -> None:
        # index 위치의 값이 diff만큼 변했을 때,
        # 그 index를 포함하는 tree 구간들에 diff를 반영

        # 이동 방향:
        # index -> index + lowbit(index)

        # 예:
        # 5 -> 6 -> 8 -> 16 ...
        while index <= self.n:
            self.tree[index] += diff
            index += self.lowbit(index)

    def prefix_sum(self, index: int) -> int:
        # 1번부터 index번까지의 합을 구함

        # 현재 tree[index]가 담당하는 구간을 더하고,
        # 그 구간을 제외한 왼쪽 prefix로 이동

        # 이동 방향:
        # index -> index - lowbit(index)

        # 예:
        # 13 -> 12 -> 8 -> 0
        total = 0

        while index > 0:
            total += self.tree[index]
            index -= self.lowbit(index)

        return total

    def update(self, index: int, val: int) -> None:
        # LeetCode index는 0-index
        # Fenwick index는 1-index

        # 기존 값과 새 값의 차이만큼만 반영
        diff = val - self.nums[index]

        # 원본 배열 값 갱신
        self.nums[index] = val

        # Fenwick Tree에는 index + 1 위치부터 diff 반영
        self.add(index + 1, diff)

    def sumRange(self, left: int, right: int) -> int:
        # sumRange(left, right)
        # = prefix_sum(right) - prefix_sum(left - 1)
        
        # 단, LeetCode는 0-index이고 Fenwick은 1-index라서
        # right는 right + 1
        # left 이전은 left

        return self.prefix_sum(right + 1) - self.prefix_sum(left)

# Brute Force:
# - update는 nums[index]만 바꾸면 되므로 O(1)
# - sumRange는 left부터 right까지 직접 더하므로 O(N)
# - 최악의 경우 3 * 10^4 * 3 * 10^4 = 9 * 10^8 연산이 발생할 수 있어 시간 초과

# Prefix Sum:
# - prefix 배열을 만들면 sumRange는 O(1)에 가능
# - 하지만 update 시 index 이후의 prefix 값을 모두 수정해야 하므로 O(N)
# - update 호출이 많으면 이것도 시간 초과 가능

# Segment Tree:
# - 각 노드가 특정 구간의 합을 저장하는 트리 구조
# - update 시 변경된 index를 포함하는 경로만 갱신
# - query 시 요청 구간과 겹치는 노드의 합만 사용
# - build O(N), update O(log N), sumRange O(log N)
# - 구현은 복잡하지만 update와 range query가 모두 많은 문제에 적합

# 풀이       
# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.n = len(nums)
#         self.nums = nums[:]  
#         self.tree = [0] * (4 * self.n)
#         self.build(1, 0, self.n - 1)

#     def build(self, node: int, start: int, end: int):
#         if start == end:
#             self.tree[node] = self.nums[start]
#             return self.tree[node]

#         mid = (start + end) // 2
        
#         left_sum = self.build(node * 2, start, mid)
#         right_sum = self.build(node * 2 + 1, mid + 1, end)

#         self.tree[node] = left_sum + right_sum

#         return self.tree[node]

#     def update_tree(self, node: int, start: int, end: int, index: int, val: int):
#         if start == end:
#             self.tree[node] = val
#             return
        
#         mid = (start + end) // 2

#         if index <= mid:
#             self.update_tree(node * 2, start, mid, index, val)
#         else:
#             self.update_tree(node * 2 + 1, mid + 1, end, index, val)

#         self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

#     def query(self, node: int, start: int, end: int, left: int, right: int) -> int:
#         if right < start or end < left:
#             return 0
#         elif left <= start and end <= right:
#             return self.tree[node]
#         else:
#             mid = (start + end) // 2

#             left_sum = self.query(node * 2, start, mid, left, right)
#             right_sum = self.query(node * 2 + 1, mid + 1, end, left, right)

#             return left_sum + right_sum


#     def update(self, index: int, val: int) -> None:
#         self.nums[index] = val
#         self.update_tree(1, 0, self.n - 1, index, val)

#     def sumRange(self, left: int, right: int) -> int:
#         return self.query(1, 0, self.n - 1, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

