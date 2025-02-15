import sys
from collections import deque

inpu=sys.stdin.readline

N=int(input())
field=[[0]*N for _ in range(N)]
K=int(input())
nowx, nowy=0,0
now=0
field[0][0]=-1
body=deque([(0, 0)])
for _ in range(K):
    tmpx, tmpy=map(int, input().split())
    tmpx-=1
    tmpy-=1
    field[tmpx][tmpy]=1

direction=[[0, 1], [1, 0], [0, -1], [-1, 0]]
tmpd=0
length=0

L=int(input())
change=deque([])
for _ in range(L):
    change.append(input().strip().split(" "))

while 1:
    now+=1
    if change and now==int(change[0][0])+1:
        s, c=change.popleft()
        if c=="D":
            tmpd=(tmpd+1)%4
        else:
            tmpd=(tmpd-1)%4
    forward=direction[tmpd]
    headx, heady=body[length][0], body[length][1]
    if 0<=headx+forward[0]<N and 0<=heady+forward[1]<N and field[headx+forward[0]][heady+forward[1]]!=-1:
        if field[headx+forward[0]][heady+forward[1]]==1:
            length+=1
        else:
            x, y=body.popleft()
            field[x][y]=0
        body.append((headx+forward[0], heady+forward[1]))
        for x, y in body:
            field[x][y]=-1

    else:
        print(now)
        sys.exit()