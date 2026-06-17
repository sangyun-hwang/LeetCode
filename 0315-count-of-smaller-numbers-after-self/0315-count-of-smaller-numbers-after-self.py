class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sorted_nums = sorted(set(nums))
        rank = {}
        answer = []

        for i, num in enumerate(sorted_nums):
            rank[num] = i + 1

        tree = [0] * (len(nums) + 1)

        def prefix_sum(index: int) -> int:
            total = 0

            while index > 0:
                total += tree[index]
                index -= index & -index

            return total

        def add(index: int, x: int):
            while index <= n:
                tree[index] += 1
                index += index & -index

        for num in reversed(nums):
            idx = rank[num]

            count = prefix_sum(idx - 1)
            answer.append(count)

            add(idx, 1)

        answer.reverse()

        return answer

        