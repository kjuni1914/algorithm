import sys
from collections import deque
input=sys.stdin.readline

land=[]
h=0

for _ in range(int(input())):
    tmp=list(map(int, input().split(" ")))
    land.append(tmp)
    if h<max(tmp):
        h=max(tmp)

move=[[1, 0], [-1, 0], [0, 1], [0, -1]]
res=1

for k in range(1, h):
    c=[[-1 for _1 in range(len(land[0]))] for _2 in range(len(land))]

    cnt=0
    queue=deque()
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j]>k and c[i][j] == -1:
                queue.append([i, j])
                c[i][j]=cnt
                while queue:
                    tmpi, tmpj = queue.popleft()
                    for m in move:
                        di, dj = tmpi+m[0], tmpj+m[1]
                        if 0<=di<len(land) and 0<=dj<len(land[0]) and land[di][dj] > k and c[di][dj]==-1:
                            queue.append([di, dj])
                            c[di][dj]=cnt
                cnt+=1
                
    if cnt>res:
        res=cnt

print(res)