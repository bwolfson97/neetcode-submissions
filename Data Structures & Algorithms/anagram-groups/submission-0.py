"""
init char_count_2_strs map
for each str: O(s)
    count chars in map O(len(str))
    if char_count map in char_count_2_strs O(len(str))
        add str to list of anagram strs
    else 
        add char_count as new key mapped to [str]
return list of values of char_count_2_strs

O(s * len(str) + s * len(str)) = O(s * len(s))

How to remove s^2 and get that down to just s?
- hash map checking is O(1) (or however long it takes to check input)
"""
class Solution:
    def _count_chars(self, s: str) -> List[int]:
        char_counts = [0] * 26
        for c in s:
            char_counts[ord(c) - ord('a')] += 1
        return tuple(char_counts)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_counts_2_anagrams = defaultdict(list)
        for s in strs:
            char_counts_2_anagrams[self._count_chars(s)].append(s)
        return list(char_counts_2_anagrams.values())
            
        