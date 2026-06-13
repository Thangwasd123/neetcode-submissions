class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_i, i in enumerate(nums):
            j_list = nums[index_i+1:]
            for index_j, j in enumerate(j_list):
                if i + j == target:
                    output_list = [index_i, index_j + index_i + 1]
                    return output_list
                else:
                    continue
