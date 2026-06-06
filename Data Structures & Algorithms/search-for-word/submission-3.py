class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = ((0,1), (1,0), (0,-1), (-1, 0))
        def dfs(r,c,i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or board[r][c] == '#'):
                return False

            board[r][c] = '#'

            for dr, dc in directions:
                res = dfs(r + dr, c + dc, i + 1)
                if res:
                    board[r][c] = word[i]
                    return res

            board[r][c] = word[i]
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
           
            

            