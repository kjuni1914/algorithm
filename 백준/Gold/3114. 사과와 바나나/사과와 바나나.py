import sys

input=sys.stdin.readline

R, C=map(int, input().split())

field=[]
for _ in range(R):
    field.append(input().rstrip().split())

pfA=[[0]*(C+1) for _ in range(R+1)]
pfB=[[0]*(C+1) for _ in range(R+1)]

for i in range(1, R+1):
    for j in range(1, C+1):
        pfA[i][j]=pfA[i][j-1]
        pfB[i][j]=pfB[i-1][j]
        if field[i-1][j-1][0]=="B":
            pfB[i][j]+=int(field[i-1][j-1][1:])
        elif field[i-1][j-1][0]=="A":
            pfA[i][j]+=int(field[i-1][j-1][1:])

revenue=[[0 for _ in range(C+1)] for _ in range(R+1)]

for i in range(1, R):
    for j in range(1, C):
        revenue[i+1][j+1]=max(revenue[i+1][j]+pfB[i][j+1], revenue[i][j+1]+pfA[i+1][j], revenue[i][j]+pfB[i][j+1]+pfA[i+1][j])

print(revenue[R][C])