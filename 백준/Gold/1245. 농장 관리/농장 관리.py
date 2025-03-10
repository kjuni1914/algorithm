import sys
from collections import deque

input=sys.stdin.readline

N, M=map(int, input().split())

field=[]
for _ in range(N):
    field.append(list(map(int, input().split())))

checked=[[False]*M for _ in range(N)]
def bfs(x, y):
    visited=[[False]*M for _ in range(N)]
    visited[x][y]=True
    checked[x][y]=True
    queue=deque([(x, y)])
    while queue:
        nowx, nowy=queue.popleft()
        h=field[nowx][nowy]
        for dx, dy in zip([1, 0, -1, 1, -1, 1, 0, -1], [-1, -1, -1, 0, 0, 1, 1, 1]):
            tmpx, tmpy=nowx+dx, nowy+dy
            if 0<=tmpx<N and 0<=tmpy<M and not visited[tmpx][tmpy]:
                if field[tmpx][tmpy]<h:
                    checked[tmpx][tmpy]=True
                    continue
                elif field[tmpx][tmpy]==h:
                    if not visited[tmpx][tmpy]:
                        queue.append((tmpx, tmpy))
                        visited[tmpx][tmpy]=True
                        checked[tmpx][tmpy]=True
                else:
                    return False
    return True

ans=0
for i in range(N):
    for j in range(M):
        if not checked[i][j] and bfs(i, j):
            ans+=1

print(ans)