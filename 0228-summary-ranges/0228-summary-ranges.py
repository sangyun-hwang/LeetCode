class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not len(nums):
            return []

        tmp = [nums[0]]
        answer = []
        start_num = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - tmp[-1] == 1:
                tmp.append(nums[i])
            else:
                if start_num == tmp[-1]:
                    answer.append(str(start_num))
                else:
                    answer.append(f"{start_num}->{tmp[-1]}")
                start_num = nums[i]
                tmp = [nums[i]]
        else:
            if start_num == tmp[-1]:
                answer.append(str(start_num))
            else:
                answer.append(f"{start_num}->{tmp[-1]}")

        return answer


        