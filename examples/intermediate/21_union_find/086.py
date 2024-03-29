class UnionFind:
    def __init__(self, n):
        self.nodes = n
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
        self.rank = [0] * n

    def find(self, i): # どの集合に属しているか（根ノードの番号）
        if self.parents[i] == i:
            return i
        else:
            self.parents[i] = self.find(self.parents[i]) # 経路圧縮
            return self.parents[i]

    def unite(self, i, j): # 二つの集合を併合
        pi = self.find(i)
        pj = self.find(j)
        if pi != pj:
            if self.rank[pi] < self.rank[pj]:
                self.sizes[pj] += self.sizes[pi]
                self.parents[pi] = pj
            else:
                self.sizes[pi] += self.sizes[pj]
                self.parents[pj] = pi
                if self.rank[pi] == self.rank[pj]:
                    self.rank[pi] += 1
    def same(self, i, j): # 同じ集合に属するかを判定
        return self.find(i)==self.find(j)

    def get_parents(self): # 根ノードの一覧を取得
        for n in range(self.nodes): # findで経路圧縮する
            self.find(n)
        return self.parents

adj = []
N, M = map(int,input().split())
for m in range(M):
    a,b = map(int,input().split())
    adj.append([a-1,b-1])

ans = 0
for i in range(M): # 取り除く辺番号
    uf = UnionFind(N)
    for j in range(M):
        if (i==j): # 辺を追加しない（取り除く）
            continue
        uf.unite(*adj[j])

    if len(set(uf.get_parents()))!=1: # 複数の集合にわかれているか確認
        ans += 1
print (ans)

# My answer
# 2021/05/04
# class UnionFind:
#     def __init__(self, n):
#         self.nodes = n
#         self.parents = [i for i in range(n)]
#         self.sizes = [1] * n
#         self.rank = [0] * n
#
#     def find(self, i):
#         if self.parents[i] == i:
#             return i
#         else:
#             self.parents[i] = self.find(self.parents[i])
#             return self.parents[i]
#
#     def unite(self, i, j):
#         pi = self.find(i)
#         pj = self.find(j)
#         if pi != pj: # この判定を忘れない
#             if self.rank[pi] > self.rank[pj]:
#                 self.sizes[pi] += self.sizes[pj]
#                 self.parents[pj] = pi
#             else:
#                 self.sizes[pj] += self.sizes[pi]
#                 self.parents[pi] = pj
#                 if self.rank[pi] == self.rank[pj]:
#                     self.rank[pj] += 1
#
#     def same(self, i, j):
#         return self.find(i) == self.find(j)
#
#     def get_parents(self):
#         for n in range(self.nodes): # 全てのノードの経路圧縮を行う
#             self.find(n)
#         return self.parents
#
# N, M = map(int, input().split())
# edges = [tuple(map(int, input().split())) for _ in range(M)]
# ans = 0
#
# for removed_edge in edges:
#     uf = UnionFind(N)
#
#     for edge in edges:
#         if edge == removed_edge: continue
#         a, b = edge
#         uf.unite(a-1, b-1)
#
#     if len(set(uf.get_parents())) > 1: ans += 1
#
# print(ans)

# 2021/05/06
# class UnionFind:
#     def __init__(self, n):
#         self.node = n
#         self.parents = [i for i in range(n)]
#         self.sizes = [1] * n
#         self.rank = [0] * n
#
#     def find(self, i):
#         if self.parents[i] == i:
#             return i
#         else:
#             self.parents[i] = self.find(self.parents[i])
#             return self.parents[i]
#
#     def unite(self, i, j):
#         pi = self.find(i)
#         pj = self.find(j)
#         if pi == pj: return
#
#         if self.rank[pi] < self.rank[pj]:
#             self.parents[pi] = pj
#             self.sizes[pj] += self.sizes[pi]
#         else:
#             self.parents[pj] = pi
#             self.sizes[pi] += self.sizes[pj]
#             if self.rank[pi] == self.rank[pj]:
#                 self.rank[pi] += 1
#
#     def same(self, i, j):
#         return self.find(i) == self.find(j)
#
#     def get_parents(self):
#         for i in range(self.node):
#             self.find(i)
#         return self.parents
#
# N, M = map(int, input().split())
# edges = [tuple(map(int, input().split())) for _ in range(M)]
# ans = 0
#
# for removed_edge in edges:
#     uf = UnionFind(N)
#     for edge in edges:
#         if removed_edge == edge: continue
#         a, b = edge
#         uf.unite(a-1, b-1)
#     if len(set(uf.get_parents())) > 1: ans += 1
#
# print(ans)

# 2021/05/19
# N, M = map(int, input().split())
# edges = [tuple(map(int, input().split())) for _ in range(M)]
#
# class UnionFind:
#     def __init__(self, n):
#         self.nodes = n
#         self.parents = [i for i in range(n)]
#         self.rank = [0]*n
#         self.sizes = [1]*n
#
#     def find(self, i):
#         if self.parents[i] == i:
#             return i
#         else:
#             self.parents[i] = self.find(self.parents[i])
#             return self.parents[i]
#
#     def unite(self, i, j):
#         pi = self.find(i)
#         pj = self.find(j)
#
#         if self.rank[pj] > self.rank[pi]:
#             self.parents[pi] = pj
#             self.sizes[pj] += self.sizes[pi]
#         else:
#             self.parents[pj] = pi
#             self.sizes[pi] += self.sizes[pj]
#             if self.rank[pj] == self.rank[pi]:
#                 self.rank[pi] += 1
#
#     def same(self, i, j):
#         return self.find(i) == self.find(j)
#
#     def get_parents(self):
#         for i in range(self.nodes):
#             self.find(i)
#         return self.parents
# ans = 0
#
# for removed_edge in edges:
#     uf = UnionFind(N)
#     for edge in edges:
#         if edge == removed_edge: continue
#
#         s, t = edge
#         uf.unite(s-1, t-1)
#     if len(set(uf.get_parents())) > 1: ans += 1
#
# print(ans)
