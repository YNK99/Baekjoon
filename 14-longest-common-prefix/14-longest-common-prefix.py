class Solution(object):
    def longestCommonPrefix(self, strs):
        L = []
        for s in strs:
            L.append(len(s))
        is_same = []
        for i in range(min(L), 0, -1):
            for s in strs:
                is_same.append(s[:i])
            if len(set(is_same)) == 1:
                break
            else:
                is_same = []
        if len(is_same) == 0:
            return ""
        else:
            return is_same[0]
        