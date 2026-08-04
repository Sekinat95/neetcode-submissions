class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        for word in strs:
            matched = False

            for subg in res:
                if Counter(word)==Counter(subg[0]):
                    matched = True
                    subg.append(word)
                    break

            if not matched:
                res.append([word])
        return res