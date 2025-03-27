import sys

N, M=map(int, input().split())

field=[]
for _ in range(N):
    field.append(list(map(int, input().split())))

def simul(x, y):
    tmpres=0

    if x<N-3:
        tmpres=max(tmpres, field[x][y]+field[x+1][y]+field[x+2][y]+field[x+3][y])
    if y<M-3:
        tmpres=max(tmpres, sum(field[x][y:y+4]))

    if x<N-1 and y<M-1:
        tmpres=max(tmpres, sum(field[x][y:y+2])+sum(field[x+1][y:y+2]))

    if x<N-1 and y<M-2:
        tmpres=max(tmpres, sum(field[x][y:y+3])+field[x+1][y+1])
    if 0<x and y<M-2:
        tmpres=max(tmpres, sum(field[x][y:y+3])+field[x-1][y+1])
    if x<N-2 and y<M-1:
        tmpres=max(tmpres, field[x][y]+field[x+1][y]+field[x+2][y]+field[x+1][y+1])
    if x<N-2 and 0<y:
        tmpres=max(tmpres, field[x][y]+field[x+1][y]+field[x+2][y]+field[x+1][y-1])

    if x<N-1 and y<M-2:
        tmpres=max(tmpres, sum(field[x][y:y+2])+sum(field[x+1][y+1:y+3]))
    if x<N-2 and y<M-1:
        tmpres=max(tmpres, field[x][y]+sum(field[x+1][y:y+2])+field[x+2][y+1])
    if 0<x and y<M-2:
        tmpres=max(tmpres, sum(field[x-1][y+1:y+3])+sum(field[x][y:y+2]))
    if 1<x and y<M-1:
        tmpres=max(tmpres, field[x-2][y+1]+sum(field[x-1][y:y+2])+field[x][y])

    if x<N-2 and 0<y:
        tmpres=max(tmpres, field[x+1][y-1]+field[x][y]+field[x+1][y]+field[x+2][y])
    if x<N-1 and y<M-2:
        tmpres=max(tmpres, sum(field[x][y:y+3])+field[x+1][y])
    if x<N-2 and y<M-1:
        tmpres=max(tmpres, field[x][y]+field[x+1][y]+field[x+2][y]+field[x][y+1])
    if 0<x and y<M-2:
        tmpres=max(tmpres, sum(field[x][y:y+3])+field[x-1][y])
    if 1<x and y<M-1:
        tmpres=max(tmpres, field[x-2][y]+field[x-1][y]+field[x][y]+field[x][y+1])
    if 0<x and 1<y:
        tmpres=max(tmpres, sum(field[x][y-2:y+1])+field[x-1][y])
    if 1<x and 0<y:
        tmpres=max(tmpres, field[x-2][y]+field[x-1][y]+field[x][y]+field[x][y-1])
    if x<N-1 and 1<y:
        tmpres=max(tmpres, sum(field[x][y-2:y+1])+field[x+1][y])
    if x<N-2 and 0<y:
        tmpres=max(tmpres, field[x][y]+field[x+1][y]+field[x+2][y]+field[x][y-1])
        
    return tmpres

res=0
for i in range(N):
    for j in range(M):
        res=max(res, simul(i, j))

print(res)
