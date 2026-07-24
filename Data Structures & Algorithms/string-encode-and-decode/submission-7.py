class Solution:

    # Time: O(m)
    # Space: O(m)
    # where 'm' is the total number of characters.
    def encode(self, strs: List[str]) -> str:
        # one line code -> return "".join(f"{len(s):03d}{s}" for s in strs)
        res = []
        for s in strs:
            length = str(len(s)).zfill(3)
            res.append(length + s)
            # or -> res.append(f"{len(s):03d}{s}")

        return "".join(res)
            
    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        k = 3
        while start < len(s) - 1:
            end = start + k
            length = s[start:end]
            start = end
            end = start + int(length)
            res.append(s[start:end])
            start = end

        return res