class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
    def find(self, x: int) -> int:
        if self.parent[x] !=  x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if self.size[rootX] < self.size[rootY]:
            rootX, rootY = rootY, rootX

        self.parent[rootY] = rootX
        self.size[rootX] += self.size[rootY]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        components = n

        for a, b in edges:
            if dsu.union(a, b):
                components -= 1

        return components