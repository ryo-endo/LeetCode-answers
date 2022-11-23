from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for i, c in enumerate(strs[0]):
            for str in strs:
                if str[i:i + 1] != c:
                    return prefix

            prefix += c

        return prefix
