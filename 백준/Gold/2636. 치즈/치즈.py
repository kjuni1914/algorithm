import sys
from collections import deque

input=sys.stdin.readline

N, M=map(int, input().split())
field=[]
queue=deque()
for i in range(N):
    field.append(list(map(int, input().split())))

def melt(x, y, i):
    visited=[[-1]*M for _ in range(N)]
    visited[x][y]=0
    queue=deque([(x, y)])
    while queue:
        for _ in range(len(queue)):
            nowx, nowy=queue.popleft()
            for dx, dy in zip([0, 0, -1, 1], [1, -1, 0, 0]):
                tmpx, tmpy=nowx+dx, nowy+dy
                if 0<=tmpx<N and 0<=tmpy<M:
                    if visited[tmpx][tmpy]==-1:
                        if field[tmpx][tmpy]==0:
                            visited[tmpx][tmpy]=0
                            queue.append((tmpx, tmpy))
                        elif field[tmpx][tmpy]==1:
                            field[tmpx][tmpy]=0
                            visited[tmpx][tmpy]=i

    return visited

visited=[[False]*M for _ in range(N)]

cnt=0
flag=True
while flag:
    flag=False
    cnt+=1
    res=melt(0, 0, cnt)
    for i in range(N):
        for j in range(M):
            if field[i][j]==1:
                flag=True
                break
        if flag:
            break

ans=0
for i in range(N):
    for j in range(M):
        if res[i][j]==cnt:
            ans+=1
if ans:
    print(cnt)
    print(ans)
else:
    print(0)
    print(0)