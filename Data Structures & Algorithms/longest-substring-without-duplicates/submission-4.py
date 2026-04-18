class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, r = 0, 0
        max_len = 0

        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r]) #[w,]
            length = (r - l) + 1
            max_len = max(max_len, length)
            r += 1
        #print(charSet)
        return max_len

                

            