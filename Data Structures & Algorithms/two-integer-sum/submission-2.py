class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_and_value = [(index, value) for index, value in enumerate(nums)]
        index_and_value.sort(key=lambda x: x[1])
        start = 0
        end = len(nums)-1

        while start < end:
            sums = index_and_value[start][1] + index_and_value[end][1]
            if (sums > target):
                end = end - 1
            elif (sums < target):
                start = start + 1
            elif (sums == target):
                return sorted([index_and_value[start][0], index_and_value[end][0]])