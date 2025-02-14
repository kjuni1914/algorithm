import sys
sys.setrecursionlimit(10**8)

input=sys.stdin.readline

field=[]
M, N=map(int, input().split())

for i in range(M):
    field.append(list(map(int, input().split())))

visited=[[-1 for _ in range(N)] for _ in range(M)]

def dfs(x, y):
    if x==M-1 and y==N-1: return 1
    if visited[x][y]!=-1:
        return visited[x][y]
    visited[x][y]=0
    for dx, dy in zip([1, -1, 0, 0], [0, 0, 1, -1]):
        if 0<=x+dx<M and 0<=y+dy<N and field[x][y]>field[x+dx][y+dy]:
            visited[x][y]+=dfs(x+dx, y+dy)
    
    return visited[x][y]

print(dfs(0, 0))