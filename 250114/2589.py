import sys
from collections import deque

input=sys.stdin.readline
h, w=map(int, input().split(" "))

world=[]
for _ in range(h):
    tmp=[]
    for i in input():
        if i=="\n":continue
        tmp.append(i)
    world.append(tmp)

move=[(1, 0), (-1, 0), (0, 1), (0, -1)]
res=0

for i in range(h):
    for j in range(w):
        queue = deque()
        visited=[[-1 for _1 in range(w)] for _ in range(h)]
        visited[i][j]=0
        if world[i][j]=="L":
            queue.append([i, j])
            
            while queue:
                nowi, nowj=queue.popleft()
                for m in move:
                    tmpi, tmpj=nowi+m[0], nowj+m[1]
                    if 0<=tmpi<len(world) and 0<=tmpj<len(world[0]) and world[tmpi][tmpj]=="L" and visited[tmpi][tmpj]==-1:
                        queue.append([tmpi, tmpj])
                        visited[tmpi][tmpj]=visited[nowi][nowj]+1
                        if res<visited[tmpi][tmpj]:
                            res=visited[tmpi][tmpj]

print(res)