class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []

        for s in strs:
            separator = str(len(s)).zfill(3)
            parts.append(separator + s)

        return "".join(parts)

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