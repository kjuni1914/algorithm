import sys
from collections import deque

input=sys.stdin.readline
N, M=map(int, input().split())

field=[]
for i in range(N):
    field.append(list(input().rstrip()))

visited=[[[-1]*2 for _ in range(M)] for _ in range(N)]

def bfs(x, y):
    queue=deque([(x, y, False)])
    visited[x][y][0]=1
    while queue:
        nowx, nowy, used=queue.popleft()
        for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            tmpx, tmpy= nowx+dx, nowy+dy

            if 0<=tmpx<N and 0<=tmpy<M:
                if not used:
                    if field[tmpx][tmpy]=="0":
                        if visited[tmpx][tmpy][0]==-1:
                            queue.append((tmpx, tmpy, False))
                            visited[tmpx][tmpy][0]=visited[nowx][nowy][0]+1
                    else:
                        if visited[tmpx][tmpy][1]==-1:
                            queue.append((tmpx, tmpy, True))
                            visited[tmpx][tmpy][1]=visited[nowx][nowy][0]+1
                else:
                    if field[tmpx][tmpy]=="0" and visited[tmpx][tmpy][1]==-1:
                        queue.append((tmpx, tmpy, True))
                        visited[tmpx][tmpy][1]=visited[nowx][nowy][1]+1

bfs(0, 0)
visited[N-1][M-1].sort()
if visited[N-1][M-1][0]!=-1:
    print(visited[N-1][M-1][0])
else:
    print(visited[N-1][M-1][1])