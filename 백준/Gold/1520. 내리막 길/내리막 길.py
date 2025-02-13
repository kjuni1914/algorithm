import sys

input=sys.stdin.readline
sys.setrecursionlimit(100000000)

M, N=map(int, input().split())

field=[]
for _ in range(M):
    field.append(list(map(int, input().split())))

visited=[[-1 for _ in range(N)] for _ in range(M)]
def dfs(x ,y):
    if x==M-1 and y==N-1:
        return 1


    if visited[x][y]==-1:
        visited[x][y]=0
        for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            if 0<=x+dx<M and 0<=y+dy<N:
                if field[x+dx][y+dy]<field[x][y]:
                    visited[x][y]+=dfs(x+dx, y+dy)
    else:
        return visited[x][y]
    return visited[x][y]

print(dfs(0 ,0))