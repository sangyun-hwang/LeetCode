## 2026.06.16

# - Problem: 307. Range Sum Query - Mutable
# - Topic: Fenwick Tree / Segment Tree
# - Reason: 동적 업데이트 + 구간 조회 연습. 코테 4번 장애물 구간 체크 문제와 연결됨.
# - Goal: Fenwick Tree의 update / prefix_sum / range_sum 구조 익히기

class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]  
        self.tree = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1)

    def build(self, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = self.nums[end]
            return self.tree[node]

        mid = (start + end) // 2
        
        left_sum = self.build(node * 2, start, mid)
        right_sum = self.build(node * 2 + 1, mid + 1, end)

        self.tree[node] = left_sum + right_sum

        return self.tree[node]

    def update_tree(self, node: int, start: int, end: int, index: int, val: int):
        if start == end:
            self.tree[node] = val
            return
        
        mid = (start + end) // 2

        if index <= mid:
            self.update_tree(node * 2, start, mid, index, val)
        else:
            self.update_tree(node * 2 + 1, mid + 1, end, index, val)

        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if right < start or end < left:
            return 0
        elif left <= start and end <= right:
            return self.tree[node]
        else:
            mid = (start + end) // 2

            left_sum = self.query(node * 2, start, mid, left, right)
            right_sum = self.query(node * 2 + 1, mid + 1, end, left, right)

            return left_sum + right_sum


    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        self.update_tree(1, 0, self.n - 1, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.query(1, 0, self.n - 1, left, right)

# Brute Force 접근
# - update: 해당 index 값을 바로 바꾸므로 O(1)
# - sumRange: left부터 right까지 직접 순회하므로 O(N)
# - 최악의 경우 nums.length와 호출 횟수가 모두 3 * 10^4까지 가능해서
#   O(N * Q) = 9 * 10^8 수준의 연산이 발생할 수 있음
# - 따라서 로직은 맞지만 시간 초과 발생

# 다음으로 생각한 Prefix Sum 접근
# - prefix 배열을 만들어두면 sumRange는 O(1)에 계산 가능
# - 하지만 update가 발생하면 index 이후의 prefix 값을 모두 수정해야 하므로 O(N)
# - update와 sumRange가 모두 많이 호출될 수 있기 때문에 이 방식도 최악의 경우 시간 초과 가능
# - 최종적으로는 Fenwick Tree / Segment Tree처럼 update와 range query를 모두 O(log N)에 처리하는 구조가 필요
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

