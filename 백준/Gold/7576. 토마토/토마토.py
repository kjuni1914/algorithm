import sys
from collections import deque

input=sys.stdin.readline

M, N=map(int, input().split())

field=[]
for i in range(N):
    field.append(list(map(int, input().split())))

def bfs(init):
    res=1000000
    queue=deque(init)
    visited=[[False]*M for _ in range(N)]
    cnt=0
    while queue:
        for _ in range(len(queue)):
            nowx, nowy=queue.popleft()
            visited[nowx][nowy]=True
            for dx, dy in zip([0, 0, -1, 1], [1, -1, 0, 0]):
                tmpx, tmpy=nowx+dx, nowy+dy
                if 0<=tmpx<N and 0<=tmpy<M and visited[tmpx][tmpy]==False and field[tmpx][tmpy]==0:
                    visited[tmpx][tmpy]=True
                    queue.append((tmpx, tmpy))
                    field[tmpx][tmpy]=1
                    if res>cnt:
                        res=cnt
        cnt+=1
    for i in range(N):
        if 0 in field[i]:
            return -1
    return cnt-1

init=[]
for i in range(N):
    for j in range(M):
        if field[i][j]==1:
            init.append((i, j))

print(bfs(init))