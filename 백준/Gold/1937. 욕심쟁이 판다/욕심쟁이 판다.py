import sys
sys.setrecursionlimit(10**9)

input=sys.stdin.readline

N=int(input())

field=[]

for i in range(N):
    field.append(list(map(int, input().split())))

visited=[[-1]*N for _ in range(N)]

def dfs(x, y):
    if visited[x][y]!=-1:
        return visited[x][y]
    res=1
    for dx, dy in zip([0, 0, -1, 1], [1, -1, 0, 0]):
        tmpx, tmpy=x+dx, y+dy
        if 0<=tmpx<N and 0<=tmpy<N and field[x][y]<field[tmpx][tmpy]:
            tmpvalue=dfs(tmpx, tmpy)+1
            if res<tmpvalue:
                res=tmpvalue
    visited[x][y]=res
    
    return visited[x][y]

res=0
for i in range(N):
    for j in range(N):
        value=dfs(i, j)
        if value>res:
            res=value
print(res)