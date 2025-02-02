import sys
input=sys.stdin.readline
import copy
from collections import deque

N, M, H=map(int, input().split())

if M==0:
    print(0)

field={i+1:set() for i in range(N)}
for i in range(M):
    h, st=map(int, input().split())
    field[st].add((h, st+1))
    field[st+1].add((h, st))

field=(field, 0, set())
def play(field):
    res=[]
    for i in range(1, N+1):
        st=i
        now=[0, i]
        while now[0]!=H+1:
            now[0]+=1
            for j in field[0][now[1]]:
                if j[0]==now[0]:
                    now=[j[0], j[1]]
                    break
        res.append((st, now[1]))
        res.sort(key=lambda x:-abs(x[1]-x[0]))
    return res
searched=set()

def change(field):
    save=copy.deepcopy(field)
    load=lambda:copy.deepcopy(save)
    state=play(field)
    res=[]
    if max([abs(i[1]-i[0]) for i in state])>3-save[1]:
        return res
    elif max([abs(i[1]-i[0]) for i in state])==0:
        print(save[1])
        sys.exit()

    for i in state:
        for h in range(1, H+1):
            tmpfield, cnt, appended=load()
            if i[0]<i[1] and (h, i[1]-1) not in appended:
                if (h, i[1]-1) not in tmpfield[i[1]]:
                    tmpfield[i[1]].add((h, i[1]-1))
                    tmpfield[i[1]-1].add((h, i[1]))
                    appended.add((h, i[1]-1))
                    res.append((tmpfield, cnt+1, appended))
                else: continue
            elif i[0]>i[1] and (h, i[1]+1) not in appended:
                if (h, i[1]+1) not in tmpfield[i[1]]:
                    tmpfield[i[1]].add((h, i[1]+1))
                    tmpfield[i[1]+1].add((h, i[1]))
                    appended.add((h, i[1]+1))
                    res.append((tmpfield, cnt+1, appended))
                else: continue
            else:
                continue
    return res

start=deque([field])
while start:
    for _ in range(len(start)):
        tmp=start.popleft()
        start.extend(change(tmp))

print(-1)