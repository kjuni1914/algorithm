import sys

input=sys.stdin.readline

R, C=map(int, input().split())

field=[["00"]*(C+1)]
for _ in range(R):
    field.append(["00"]+input().rstrip().split())

pfA=[[0]*(C+1) for _ in range(R+1)]
pfB=[[0]*(C+1) for _ in range(R+1)]

for i in range(R+1):
    for j in range(C+1):
        pfA[i][j]=pfA[i][j-1]
        pfB[i][j]=pfB[i-1][j]
        if field[i][j][0]=="B":
            pfB[i][j]+=int(field[i][j][1:])
        elif field[i][j][0]=="A":
            pfA[i][j]+=int(field[i][j][1:])

revenue=[[0*3 for _ in range(C+1)] for _ in range(R+1)]

for i in range(2, R+1):
    for j in range(2, C+1):
        revenue[i][j]=max(revenue[i][j-1]+pfB[i-1][j], revenue[i-1][j]+pfA[i][j-1], revenue[i-1][j-1]+pfB[i-1][j]+pfA[i][j-1])

print(revenue[R][C])