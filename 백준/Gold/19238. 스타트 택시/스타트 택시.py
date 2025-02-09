import sys
from collections import deque

input=sys.stdin.readline

N, M, fuel=map(int, input().split())

field=[]

for i in range(N):
    tmp=list(map(int, input().split()))
    for j in range(N):
        if tmp[j]==1:
            tmp[j]="X"
    field.append(tmp)

tmp=1
nowx, nowy=map(int, input().split())
nowx-=1
nowy-=1
nowfuel=fuel
customer=[]
destination=[]

for i in range(M):
    x, y, ox, oy=map(int, input().split())
    customer.append((x-1, y-1))
    destination.append((ox-1, oy-1))
    tmp+=1

def bfs(i, j):
    visited=[[-1 for _ in range(N)] for _ in range(N)]
    queue=deque([(i, j)])
    visited[i][j]=0
    while queue:
        nowx, nowy=queue.popleft()
        for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            if 0<=nowx+dx<N and 0<=nowy+dy<N and visited[nowx+dx][nowy+dy]==-1 and isinstance(field[nowx+dx][nowy+dy], int):
                queue.append((nowx+dx, nowy+dy))
                visited[nowx+dx][nowy+dy]=visited[nowx][nowy]+1
    return visited

while nowfuel and customer:
    distance=bfs(nowx, nowy)
    tmpdis=float("inf")
    idx=0
    for i in range(len(customer)):
        cusx, cusy=customer[i]
        if 0<=distance[cusx][cusy]<tmpdis:
            tmpdis=distance[cusx][cusy]
            idx=i
        elif distance[cusx][cusy]==tmpdis:
            if cusx<customer[idx][0]:
                idx=i
            elif cusx==customer[idx][0]:
                if cusy<customer[idx][1]:
                    idx=i
    cusx, cusy=customer[idx]
    if tmpdis<=nowfuel:
        nowx, nowy=cusx, cusy
        nowfuel-=tmpdis
    else:
        print(-1)
        sys.exit()
    distance=bfs(nowx, nowy)

    obx, oby=destination[idx]
    if 0<=distance[obx][oby]<=nowfuel:
        nowfuel+=distance[obx][oby]
        nowx, nowy=obx, oby
    else:
        print(-1)
        sys.exit()
        
    customer.pop(idx)
    destination.pop(idx)

print(nowfuel)