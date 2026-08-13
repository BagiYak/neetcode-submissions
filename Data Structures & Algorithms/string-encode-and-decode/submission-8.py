class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            separator = str(len(s)).zfill(3)
            res += separator + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        pref = 3
        while start < len(s):
            length = s[start:start + pref]
            start = start + pref
            end = start + int(length)
            word = s[start:end]
            res.append(word)
            start = end

        return res