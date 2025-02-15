import sys
from collections import deque

input=sys.stdin.readline

N=int(input())

field=[]
flag1=0
flag2=0
for i in range(N):
    tmp=input().strip()
    tmp2=[]
    for j in range(N):
        tmp2.append(tmp[j])
        if tmp[j]=="B":
            tmp2[j]="0"
            if flag1==1:
                bx, by=i, j
            flag1+=1
            tmpbx, tmpby=i, j
        elif tmp[j]=="E":
            tmp2[j]="0"
            if flag2==1:
                ex, ey=i, j
            flag2+=1
            tmpex, tmpey=i, j
    field.append(tmp2)

if tmpbx==bx:
    state=0
else:
    state=1
if tmpex==ex:
    endstate=0
else:
    endstate=1

visited=[[[-1  for _ in range(2)] for _ in range(N)] for _ in range(N)]

def bfs(x, y, state):
    visited[x][y][state]=0
    queue=deque([(x, y, state)])
    while queue:
        nowx, nowy, nowstate=queue.popleft()
        turn=visited[nowx][nowy][nowstate]
        if nowx==ex and nowy==ey and nowstate==endstate:
            print(turn)
            sys.exit()
        for dx, dy in zip([0, 0, -1, 1], [1, -1, 0, 0]):
            tmpx, tmpy=nowx+dx, nowy+dy
            if nowstate==1: # 세로
                if canmove(tmpx, tmpy, nowstate, (dx, dy)) and visited[tmpx][tmpy][nowstate]==-1:
                    queue.append((tmpx, tmpy, nowstate))
                    visited[tmpx][tmpy][nowstate]=turn+1
            else: # 가로
                if canmove(tmpx, tmpy, nowstate, (dx, dy)) and visited[tmpx][tmpy][nowstate]==-1:
                    queue.append((tmpx, tmpy, nowstate))
                    visited[tmpx][tmpy][nowstate]=turn+1
        if canrotate(nowx, nowy) and visited[nowx][nowy][(nowstate+1)%2]==-1:
            queue.append((nowx, nowy, (nowstate+1)%2))
            visited[nowx][nowy][(nowstate+1)%2]=turn+1
            
    print(0)
    sys.exit()


def canrotate(x, y):
    for dx, dy in zip([-1, -1, -1, 0, 0, 1, 1, 1], [-1, 1, 0, -1, 1, -1, 0, 1]):
        if not (0<=x+dx<N and 0<=y+dy<N and field[x+dx][y+dy]=="0"):
            return False
    return True

def canmove(x, y, state, direction):
    dx, dy=direction
    if state==1:
        if dx:
            if not (0<=x+dx<N and field[x+dx][y]=="0"):
                return False
        else:
            for i in [-1, 0, 1]:
                if not (0<=y<N and field[x+i+dx][y]=="0"):
                    return False
    else:
        if dy:
            if not (0<=y+dy<N and field[x][y+dy]=="0"):
                return False
        else:
            for i in [-1, 0, 1]:
                if not (0<=x<N and field[x][y+i+dy]=="0"):
                    return False
    return True

bfs(bx, by, state)