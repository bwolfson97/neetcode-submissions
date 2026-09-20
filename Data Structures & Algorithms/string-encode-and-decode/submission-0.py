class Solution:
    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(f"{len(s)}:")
            parts.append(s)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        size_start = 0
        strs = []
        while size_start < len(s):
            delimiter = s.index(":", size_start)
            size = int(s[size_start:delimiter])
            word_start = delimiter + 1
            strs.append(s[word_start : word_start + size])
            size_start = word_start + size
        return strs

"""
0:
s
 d
  w

size: 1
"""