class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        answer = []

        tmp = intervals[0]

        for i in range(1, len(intervals)):
            if tmp[1] >= intervals[i][0]:
                if tmp[1] < intervals[i][1]:
                    tmp = [tmp[0], intervals[i][1]]
            else:
                answer.append(tmp)
                tmp = intervals[i]

        answer.append(tmp)

        return answer
        