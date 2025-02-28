import sys
from collections import deque

input=sys.stdin.readline

M, N, H=map(int, input().split())

field=[]
tomato=deque()
for z in range(H):
    tmp=[]
    for y in range(N):
        tmp.append(list(map(int, input().split())))
        for x in range(M):
            if tmp[y][x]==1:
                tomato.append((x, y, z))
    field.append(tmp)

def bfs(queue):
    while queue:
        for _ in range(len(queue)):
            nowx, nowy, nowz=queue.popleft()
            for dx, dy, dz in zip([1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]):
                tmpx, tmpy, tmpz=nowx+dx, nowy+dy, nowz+dz
                if 0<=tmpx<M and 0<=tmpy<N and 0<=tmpz<H:
                    if field[tmpz][tmpy][tmpx]==0:
                        field[tmpz][tmpy][tmpx]=field[nowz][nowy][nowx]+1
                        queue.append((tmpx, tmpy, tmpz))

bfs(tomato)
ans=0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if field[z][y][x]!=0:
                if ans<field[z][y][x]:
                    ans=field[z][y][x]
            else:
                print(-1)
                sys.exit()

print(ans-1)