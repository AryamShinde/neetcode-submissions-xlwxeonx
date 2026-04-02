'''
parent = [0,0,0,3,3]

unique = {0, 3}

[0, 1] 0 -> 1, 1 -> 0, merge them 1 -> 0
[1, 2] 1 -> 0, 2 -> 1, merge 2 -> 0 parent[2] = 0
[3, 4] 3 -> 4, 4 -> 3, merge 4 -> 3, parent[4] = 3
'''
class UnionFind:
    def __init__(self, n): #[[[0,1],[1,2],[3,4]]]
        self.parent = list(range(n)) # parent = [0,1,2,3,4]
        self.count = n # count = 5

    def find(self, x):
        if self.parent[x] != x: 
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rootA = self.find(a) # 0 -> 0
        rootB = self.find(b) # 1 -> 1

        if rootA != rootB: # 1 != 0
            self.parent[rootB] = rootA # 1 -> 0
            self.count -= 1 # 5 - 1 = 4


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for u, v in edges:
            uf.union(u, v)

        return uf.count