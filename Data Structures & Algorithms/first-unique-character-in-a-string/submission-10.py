class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = dict(Counter(s))
        #print(dict(counter))
        for char in s:
            if counter[char] > 1:
                pass
            elif counter[char]==1:
                return s.index(char)
        return -1