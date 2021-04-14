import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1E+7))
def main():
    N, Q = map(int, input().split())
    link = [[] for _ in range(N+1)]
    for n in range(N-1):
        a, b = map(int, input().split())
        link[a].append(b)
        link[b].append(a)
    V = [0] * (N+1)
    for q in range(Q):
        p, x = map(int, input().split())
        V[p] += x # `操作`の際の根に当たるノードのカウンター`V`に先に値を加算する。

    def dfs(i, parent, acc): # 深さ優先探索
        V[i] += acc # 親ノードまでの累積値を加算
        for j in link[i]:
            if j != parent: # 親ノードを追加しない
                dfs(j,i,V[i])
    cur = 1
    parent = 0
    acc = 0
    dfs(cur, parent , acc) # 親ノードを0としてスタート
    V = [str(v) for v in V]
    print (" ".join(V[1:]))

if __name__ == '__main__':
    main()
