import sys
input=sys.stdin.readline

N=int(input())
field=[]
students=[]
for i in range(N):
    field.append(list(input().rstrip().split()))
    for j in range(N):
        if field[i][j]=="S":
            students.append((i, j))

def check():
    for x, y in students:
        for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
            tmpx, tmpy=x, y
            while 0<=tmpx<N and 0<=tmpy<N:
                if field[tmpx][tmpy]=="T":
                    return
                elif field[tmpx][tmpy]=="O":
                    break
                else:
                    tmpx+=dx
                    tmpy+=dy
                    continue
    print("YES")
    sys.exit()


def backtracking():
    for i in range(N**2-2):
        if field[i//N][i%N]!="X":
            continue
        for j in range(i+1, N**2-1):
            if field[j//N][j%N]!="X":
                continue
            for k in range(j+1, N**2):
                if field[k//N][k%N]!="X":
                    continue
                field[i//N][i%N]="O"
                field[j//N][j%N]="O"
                field[k//N][k%N]="O"
                check()
                field[i//N][i%N]="X"
                field[j//N][j%N]="X"
                field[k//N][k%N]="X"

backtracking()
print("NO")