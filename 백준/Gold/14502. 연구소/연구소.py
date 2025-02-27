import sys
from collections import deque

input=sys.stdin.readline
N, M=map(int, input().split())

field=[]
queue=[]
wall=0
for i in range(N):
    tmp=list(map(int, input().split()))
    field.append(tmp)
    for j in range(M):
        if tmp[j]==2:
            queue.append((i, j))
        elif tmp[j]==1:
            wall+=1

def bfs(queue, field):
    visited=[[-1 for _ in range(M)] for _ in range(N)]
    for x, y in queue:
        visited[x][y]=0

    while queue:
        for _ in range(len(queue)):
            nowx, nowy=queue.popleft()
            for dx, dy in zip([1, -1, 0, 0], [0, 0, -1, 1]):
                tmpx, tmpy=nowx+dx, nowy+dy
                if 0<=tmpx<N and 0<=tmpy<M:
                    if visited[tmpx][tmpy]==-1 and field[tmpx][tmpy]==0:
                        visited[tmpx][tmpy]=visited[nowx][nowy]+1
                        queue.append((tmpx, tmpy))
    return visited

ans=0
for i in range(N*M-2):
    if field[i//M][i%M]!=0:
        continue
    for j in range(i+1, N*M-1):
        if field[j//M][j%M]!=0:
            continue
        for k in range(j+1, N*M):
            if field[k//M][k%M]!=0:
                continue
            field[i//M][i%M]=1
            field[j//M][j%M]=1
            field[k//M][k%M]=1
            resfield=bfs(deque(queue[:]), field)
            field[i//M][i%M]=0
            field[j//M][j%M]=0
            field[k//M][k%M]=0
            res=0
            for row in resfield:
                res+=row.count(-1)
            if ans<res:
                ans=res

print(ans-3-wall)