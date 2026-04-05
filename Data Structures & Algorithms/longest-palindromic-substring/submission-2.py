class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        longest = ""

        for i in range(len(s)):
            odd = self.expand(s, i, i)
            even = self.expand(s, i, i + 1)

            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest

    def expand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return s[l + 1: r]
        