import sys
import copy

input=sys.stdin.readline

field=[]
for _ in range(10):
    tmp=input()
    field.append([tmp[i] for i in range(10)])

def change(i, j):
    if field[i][j]=='#':
        field[i][j]='O'
    else:
        field[i][j]='#'
    orii=i
    orij=j
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        i=orii+di
        j=orij+dj
        if 0<=i<10 and 0<=j<10:
            if field[i][j]=='#':
                field[i][j]='O'
            else:
                field[i][j]='#'

save=copy.deepcopy(field)

ans=100000
for case in range(1024):
    tmpans=0
    field=copy.deepcopy(save)
    for i in range(0, len(field)):
        if i==0:
            on="".join(["0"]*(10-len(bin(case)[2:])))+bin(case)[2:]
            for k in range(len(on)):
                if on[k]=="1":
                    change(0, 9-k)
                    tmpans+=1
        else:
            for j in range(len(field[i])):
                if field[i-1][j]=="O":
                    change(i, j)
                    tmpans+=1
    if tmpans<ans and "O" not in "".join(["".join(field[_]) for _ in range(10)]):
        ans=tmpans

if ans==100000:
    print(-1)
else:
    print(ans)