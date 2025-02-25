import sys
from collections import deque

input=sys.stdin.readline

N=int(input())

field=[]
for _ in range(N):
    field.append(list(input().rstrip()))

def bfs(x, y, visited, res):
    queue=deque([(x, y)])
    cnt=1
    visited[x][y]=cnt
    while queue:
        nowx, nowy=queue.popleft()
        for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
            tmpx, tmpy=nowx+dx, nowy+dy
            if 0<=tmpx<N and 0<=tmpy<N:
                if visited[tmpx][tmpy]==-1 and field[tmpx][tmpy]=="1":
                    cnt+=1
                    visited[tmpx][tmpy]=cnt
                    queue.append((tmpx, tmpy))

    res.append(cnt)

res=[]
visited=[[-1]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if field[i][j]=="1" and visited[i][j]==-1:
            bfs(i, j, visited, res)
            
res.sort()
print(len(res))
for i in res:
    print(i)