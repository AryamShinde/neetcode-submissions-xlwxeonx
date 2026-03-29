class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_t = sorted(t)
        sort_s = sorted(s)

        if sort_s == sort_t:
            return True
        return False
