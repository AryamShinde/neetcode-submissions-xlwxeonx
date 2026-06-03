class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        c_S, c_T = {}, {}

        for i in range(len(s)):
            c_S[s[i]] = 1 + c_S.get(s[i], 0)
            c_T[t[i]] = 1 + c_T.get(t[i], 0)

        return c_S == c_T