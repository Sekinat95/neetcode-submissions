class Solution:
    def isPalindrome(self, s: str) -> bool:
        punctuation = {"?", ",","'"}
        for el in punctuation:
            if el in s:
                s = s.strip(el)

        #s = s.replace(" ", "")
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(s, s[::-1])
        #s = s.lower()
        return s == s[::-1]
        