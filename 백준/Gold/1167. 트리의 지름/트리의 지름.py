import sys
sys.setrecursionlimit(10**5)

input=sys.stdin.readline

N=int(input())

graph=[[] for _ in range(N)]
for i in range(N):
    cmd=list(map(int, input().rstrip().split()))
    for j in range((len(cmd)-2)//2):
        graph[cmd[0]-1].append([cmd[2*j+1]-1, cmd[2*j+2]])
        graph[cmd[2*j+1]-1].append([cmd[0]-1, cmd[2*j+2]])

def dfs(idx, init=False, visited=None):
    if init:
        visited=[-1]*N 
        visited[idx]=0
    for v, w in graph[idx]:
        if visited[v]==-1:
            visited[v]=w+visited[idx]
            dfs(v, False, visited)
    return visited

tmp=dfs(0, True)
tmp=[[i, idx]for idx, i in enumerate(tmp)]
tmp.sort(reverse=True)
res=dfs(tmp[0][1], True)
print(max(res))