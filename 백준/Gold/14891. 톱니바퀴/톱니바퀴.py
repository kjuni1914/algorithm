import sys

input=sys.stdin.readline

cogs=[input().rstrip() for _ in range(4)]

def turn(cogs, idx, direction, turned=None):
    if turned is None:
        turned=set()
    now=cogs[idx]
    turned.add(idx)

    if idx>0:
        left=cogs[idx-1]
        if (idx-1) not in turned and left[2]!=now[6]:
            turn(cogs, idx-1, -1*direction, turned)
    if idx<3:
        right=cogs[idx+1]
        if (idx+1) not in turned and now[2]!=right[6]:
            turn(cogs, idx+1, -1*direction, turned)

    if direction==-1:
        now=now[1:8]+now[0]
    elif direction==1:
        now=now[7]+now[0:7]
    cogs[idx]=now

for _ in range(int(input())):
    idx, direction=map(int, input().split())
    turn(cogs, idx-1, direction)

ans=0
for i in range(4):
    if cogs[i][0]=="1":
        ans+=2**(i)
print(ans)