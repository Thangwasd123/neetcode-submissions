class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output_dict = {}
        for num in nums:
            if num not in output_dict.keys():
                output_dict[num] = 1
            else:
                output_dict[num] += 1
        desc = {k: v for k,v in sorted(output_dict.items(), key = lambda item:item[1], reverse = True)}
        ouput_list = list(desc.keys())
        return ouput_list[:k]