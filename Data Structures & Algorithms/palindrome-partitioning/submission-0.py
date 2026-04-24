class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_pal(sub):
            l, r = 0, len(sub) - 1

            while l < r:
                if sub[l] != sub[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i, curr):
            if i == len(s):
                res.append(curr.copy())
                return

            for j in range(i + 1, len(s) + 1):
                piece = s[i:j]
                if is_pal(piece):
                    curr.append(piece)
                    dfs(j, curr)
                    curr.pop()

        dfs(0, [])
        return res



