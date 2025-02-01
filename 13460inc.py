import sys
from collections import deque
import copy

input=sys.stdin.readline

N, M=map(int, input().split())
field=[]

for i in range(N):
    tmp=input().strip()
    tmp2=[]
    for j in range(M):
        if tmp[j]=="R": 
            redx, redy=i, j
        elif tmp[j]=="B": bluex, bluey=i,j
        elif tmp[j]=="O": objx, objy=i, j
        else: 
            tmp2.append("#")
            continue
        tmp2.append(".")
    field.append(tmp2)

save=copy.deepcopy(field)

def bfs(x, y):
    visited=[[-1 for _ in range(M)] for _ in range(N)]
    search=deque([(x, y)])
    nowblue=deque([(bluex, bluey)])
    visited[x][y]=0
    dxs=[0, 0, 1, -1]
    dys=[1, -1, 0, 0]
    cnt=0
    while search:
        cnt+=1
        for _ in range(len(search)):
            nowx, nowy=search.popleft()
            nowbluex, nowbluey=nowblue.popleft()
            nowfield=copy.deepcopy(save)
            nowfield[nowx][nowy]="."
            nowfield[nowbluex][nowbluey]="."
            for dx, dy in zip(dxs, dys):
                tmpx, tmpy=nowx, nowy
                tmpbluex, tmpbluey=nowbluex, nowbluey
                        
                while 1:
                    if field[tmpbluex+dx][tmpbluey+dy]==".":
                        tmpbluex+=dx
                        tmpbluey+=dy
                    elif field[tmpbluex+dx][tmpbluey+dy]=="O":
                        break
                else:
                    while 1:
                        if field[tmpx+dx][tmpy+dy]=="O":
                            if visited[nowx][nowy]+1<=10:
                                print(cnt)
                            else: print(-1) 
                            return
                        if field[tmpx+dx][tmpy+dy]!=".":
                            break
                        else:
                            tmpx+=dx
                            tmpy+=dy

                    search.append((tmpx, tmpy))
                    nowblue.append((tmpbluex, tmpbluey))
                    visited[tmpx][tmpy]=cnt

        cnt+=1
            
    print(-1)


bfs(redx, redy)