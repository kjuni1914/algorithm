import sys
import copy
from collections import deque

input=sys.stdin.readline

N, M=map(int, input().split())
field=[]
for i in range(N):
    tmp=input().strip()
    tmp2=[]
    for j in range(M):
        tmp2.append(tmp[j])
    field.append(tmp2)

def findXY(field):
    for i in range(N):
        for j in range(M):
            if field[i][j]=="B":
                bx, by=i, j
            elif field[i][j]=="R":
                rx, ry=i, j
    return bx, by, rx, ry

def move(nowfields):
    for _ in range(len(nowfields)):
        field=nowfields.popleft()
        save=copy.deepcopy(field)
        nowbx, nowby, nowrx, nowry=findXY(save)
        dxs=[1, -1, 0, 0]
        dys=[0, 0, -1, 1]
        for dx, dy in zip(dxs, dys):
            state=0
            tmpfield=copy.deepcopy(save)
            bx, by, rx, ry=nowbx, nowby, nowrx, nowry

            while 1:
                if tmpfield[rx+dx][ry+dy]=="O":
                    state=1
                    tmpfield[rx][ry]="."
                if tmpfield[bx+dx][by+dy]=="O":
                    state=-1
                    break
                if tmpfield[bx+dx][by+dy]!="." and tmpfield[rx+dx][ry+dy]!=".":
                    break
                if 0<=bx+dx<N and 0<=by+dy<M and tmpfield[bx+dx][by+dy]==".":
                    tmpfield[bx][by]="."
                    tmpfield[bx+dx][by+dy]="B"
                    bx, by=bx+dx, by+dy
                if 0<=rx+dx<N and 0<=ry+dy<M and tmpfield[rx+dx][ry+dy]==".":
                    tmpfield[rx][ry]="."
                    tmpfield[rx+dx][ry+dy]="R"
                    rx, ry=rx+dx, ry+dy

            if state==0 and (nowbx!=bx or nowby!=by or nowrx!=rx or nowry!=ry):
                nowfields.append(tmpfield)

            elif state==1:
                print(iter)
                sys.exit()

now=deque([field])
iter=1
while now:
    move(now)
    iter+=1
    if iter>10:
        print(-1)
        sys.exit()
print(-1)