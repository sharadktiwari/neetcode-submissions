class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        seen = defaultdict(list)
        for word in strs:
            sword = "".join(sorted(word))
            seen[sword].append(word)
        return list(seen.values())


