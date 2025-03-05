import sys
sys.setrecursionlimit(10**6)

input=sys.stdin.readline
N=int(input())

graph=[[] for _ in range(N)]

for _ in range(N-1):
    a, b, c=map(int, input().split())
    a, b=a-1, b-1
    graph[a].append([b, c])
    graph[b].append([a, c])

def dfs(node, dist, visited):
    if visited[node]==-1:
        visited[node]=0
    for v, w in graph[node]:
        if visited[v]==-1:
            visited[v]=dist+w
            dfs(v, dist+w, visited)
    return visited

res=dfs(0, 0, [-1]*N)
res=[(v, idx) for idx, v in enumerate(res)]
res.sort(reverse=True)
res=dfs(res[0][1], 0, [-1]*N)
print(max(res))