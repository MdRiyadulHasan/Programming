from typing import List 
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
        print(self.parent)
        print(self.rank)
    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx!=rooty:
            if self.rank[rootx]>self.rank[rooty]:
                self.parent[rooty]=rootx
            elif self.rank[rootx]<self.rank[rooty]:
                self.parent[rootx]=rooty
            else:
                self.parent[rooty]=rootx
                self.rank[rootx]+=1
    def connected(self, x,y):
        return self.find(x)== self.find(y)
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)
        for u,v in edges:
            uf.union(u,v)
        return uf.connected(source, destination)
        

                

        


        