'''
[[0,1],[1,2],[3,4]]

0 <-> 1 <-> 2
3 <-> 4
'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)] #[0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3]]
        visit = set()

        for u, v in edges:#(u -> 0, v -> 1)
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node): #visit = {0, 1, 2}
            for nei in adj[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)

        res = 0
        for node in range(n):
            if node not in visit:
                visit.add(node)
                dfs(node)
                res += 1
        return res


