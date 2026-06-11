from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_items = sorted(counter.items(), key = lambda x: x[1], reverse=True)

        answer = []

        for i in range(k):
            answer.append(sorted_items[i][0])

        return answer

        