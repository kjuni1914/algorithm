import sys
from collections import deque

input = sys.stdin.readline

N=int(input())

field1=[]
field2=[]

for _ in range(N):
    cmd=input().rstrip()
    tmp1=[]
    tmp2=[]
    for j in range(N):
        tmp1.append(cmd[j])
        if cmd[j]=="R" or cmd[j]=="G":
            tmp2.append("R")
        else:
            tmp2.append(cmd[j])
    field1.append(tmp1)
    field2.append(tmp2)

visited1=[[False]*N for _ in range(N)]
visited2=[[False]*N for _ in range(N)]

def bfs(x, y, visited, field):
    if visited[x][y]:
        return False
    visited[x][y]=True
    queue=deque([(x, y)])
    while queue:
        nowx, nowy=queue.popleft()
        for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            tmpx, tmpy=nowx+dx, nowy+dy
            if 0<=tmpx<N and 0<=tmpy<N:
                if not visited[tmpx][tmpy]:
                    if field[nowx][nowy]==field[tmpx][tmpy]:
                        visited[tmpx][tmpy]=True
                        queue.append((tmpx, tmpy))
    return True

cnt1, cnt2=0, 0

for i in range(N):
    for j in range(N):
        if bfs(i, j, visited1, field1):
            cnt1+=1
        if bfs(i, j, visited2, field2):
            cnt2+=1

print(cnt1, cnt2)