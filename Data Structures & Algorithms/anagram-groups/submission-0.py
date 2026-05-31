class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map={}
        for s in strs:
            temp= tuple(sorted(s))
            if temp not in anagram_map:
                anagram_map[temp] = [s]
            else:
                anagram_map[temp].append(s)
        return list(anagram_map.values())
