class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        for s in strs:
            key = frozenset(Counter(s).items())
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]

        return list(d.values())