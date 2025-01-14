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
        if world[i][j]=="L":
            queue = deque()
            visited=[[-1 for _1 in range(w)] for _ in range(h)]
            queue.append([i, j])
            cnt=0
            visited[i][j]=cnt
            tmplist=deque()
            while queue:
                flag=False
                for _ in range(len(queue)):
                    tmplist.append(queue.popleft())
                for _2 in range(len(tmplist)):
                    nowi, nowj=tmplist.popleft()
                    for m in move:
                        tmpi, tmpj=nowi+m[0], nowj+m[1]
                        if 0<=tmpi<len(world) and 0<=tmpj<len(world[0]) and world[tmpi][tmpj]=="L" and visited[tmpi][tmpj]==-1:
                            queue.append([tmpi, tmpj])
                            visited[tmpi][tmpj]=cnt
                            flag=True
                if flag==True:
                    cnt+=1
                    
            if res<cnt:
                res=cnt

print(res)