class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = Counter(nums)
        if len(freq) == len(nums):
            return False
        
        nums_dict_index = {i:[] for i in nums}

        for ind, ele in enumerate(nums):
            nums_dict_index[ele].append(ind)
        
        for ele in freq:
            if freq[ele] > 1:
                indices = nums_dict_index[ele]
                for x in range(len(indices) - 1):
                    abs_u = 0
                    abs_u = abs(indices[x+1] - indices[x])
                    if abs_u <= k:
                        return True

        return False

        
        




        