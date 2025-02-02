import sys
from collections import deque
import copy

input=sys.stdin.readline

N, M, H=map(int, input().split())

if M==0:
    print(0)
    sys.exit()

field={i+1:set() for i in range(H)}
for _ in range(M):
    h, st=map(int, input().split())
    field[h].add((st, st+1))

def play(field):
    res=[]
    for i in range(1, N+1):
        st=i
        now=i
        for h in range(1, H+1):
            if (now, now+1) in field[h]:
                now+=1
            elif (now-1, now) in field[h]:
                now-=1
        end=now
        res.append((st, end))
    res.sort(key=lambda x:-abs(x[1]-x[0]))
    return res

field=(field, 0)

def change(field):
    save, cnt=copy.deepcopy(field)
    state=play(save)
    if cnt>3:
        return
    elif max([abs(i[0]-i[1]) for i in state])==0:
        print(cnt)
        sys.exit()
    res=[]
    for i in state:
        tmpfield=copy.deepcopy(save)
        if i[0]==i[1]: continue
        added=False
        if i[0]>i[1]: 
            for h in range(H, 0, -1):
                if (i[1]-1, i[1]) not in tmpfield[h] and (i[1], i[1]+1) not in tmpfield[h] and (i[1]+1, i[1]+2) not in tmpfield[h]:
                    tmpfield[h].add((i[1], i[1]+1))
                    added=True
                    break
        elif i[0]<i[1]:
            for h in range(H, 0, -1):
                if (i[1], i[1]+1) not in tmpfield[h] and (i[1]-1, i[1]) not in tmpfield[h] and (i[1]-2, i[1]-1) not in tmpfield[h]:
                    tmpfield[h].add((i[1]-1, i[1]))
                    added=True
                    break
        if added==True:
            res.append((tmpfield, cnt+1))
    return res

nowfields=deque([field])
while nowfields:
    for _ in range(len(nowfields)):
        nowfield=nowfields.popleft()
        tmp=change(nowfield)
        if tmp!=None:
            nowfields.extend(tmp)

print(-1)
