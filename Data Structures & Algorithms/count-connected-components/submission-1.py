'''
parent = [0,0,0,3,3]

unique = {0, 3}

[0, 1] 0 -> 1, 1 -> 0, merge them 1 -> 0
[1, 2] 1 -> 0, 2 -> 1, merge 2 -> 0 parent[2] = 0
[3, 4] 3 -> 4, 4 -> 3, merge 4 -> 3, parent[4] = 3
'''
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA != rootB:
            self.parent[rootB] = rootA
            self.count -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for u, v in edges:
            uf.union(u, v)

        return uf.count