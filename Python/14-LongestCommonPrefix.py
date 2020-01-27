class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        if not strs:
            return common
        strs.sort()
        i = 0
        while i <= len(strs[0]):
            if strs[0][:i] == strs[-1][:i]:
                common = strs[0][:i]
            i += 1
        return common
