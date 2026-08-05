class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)

        return len(freq) < len(nums)
        