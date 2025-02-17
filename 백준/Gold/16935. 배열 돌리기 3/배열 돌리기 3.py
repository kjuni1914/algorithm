import sys

input=sys.stdin.readline

N, M, R=map(int, input().split())

init=[list(input().rstrip().split()) for _ in range(N)]

change=list(input().split())

def move(updown, lright, clockwise, rotate, init):
    N, M=len(init), len(init[0])
    if updown%2:
        init=init[::-1]
    if lright%2:
        for i in range(len(init)):
            init[i]=init[i][::-1]
    while rotate%4:
        res=[[""]*M for _ in range(N)]
        for i in range(int(N/2)):
            for j in range(int(M/2)):
                res[i][j]=init[i+int(N/2)][j]
        for i in range(int(N/2)):
            for j in range(int(M/2)):
                res[i][j+int(M/2)]=init[i][j]
        for i in range(int(N/2)):
            for j in range(int(M/2)):
                res[i+int(N/2)][j]=init[i+int(N/2)][j+int(M/2)]
        for i in range(int(N/2)):
            for j in range(int(M/2)):
                res[i+int(N/2)][j+int(M/2)]=init[i][j+int(M/2)]
        init=res
        rotate-=1
    while clockwise%4:
        res=[[""]*N for _ in range(M)]
        for j in range(M):
            for i in range(N):
                res[j][i]+=init[N-i-1][j]
        init=res
        clockwise-=1
        N, M=M, N

    return init

updown=0
lright=0
clockwise=0
rotate=0
state=0

for i in change:
    if i=="1":
        if state==1:
            init=move(updown, lright, clockwise, rotate, init)
            updown, lright, clockwise, rotate=0, 0, 0, 0
        updown+=1
        state=-1
    elif i=="2":
        if state==1:
            init=move(updown, lright, clockwise, rotate, init)
            updown, lright, clockwise, rotate=0, 0, 0, 0
        lright+=1
        state=-1
    elif i=="3":
        if state==-1:
            init=move(updown, lright, clockwise, rotate, init)
            updown, lright, clockwise, rotate=0, 0, 0, 0
        clockwise+=1
        state=1
    elif i=="4":
        if state==-1:
            init=move(updown, lright, clockwise, rotate, init)
            updown, lright, clockwise, rotate=0, 0, 0, 0
        clockwise-=1
        state=1
    elif i=="5":
        if state==-1:
            init=move(updown, lright, clockwise, rotate, init)
            updown, lright, clockwise, rotate=0, 0, 0, 0
        rotate+=1
        state=1
    else:
        if state==-1:
            init=move(updown, lright, clockwise, rotate, init)
            updown, lright, clockwise, rotate=0, 0, 0, 0
        rotate-=1
        state=1

init=move(updown, lright, clockwise, rotate, init)

for i in init:
    print(" ".join(i))