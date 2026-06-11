class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        answer = [intervals[0]]

        for start, end in intervals[1:]:
            last = answer[-1]

            if start <= last[1]:
                last[1] = max(last[1], end)
            else:
                answer.append([start, end])

        return answer