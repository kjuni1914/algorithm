import sys

input=sys.stdin.readline
A=[]
B=[]
N, M=map(int, input().split())

for _ in range(N):
    A.append([int(_) for _ in str(input()) if _!='\n'])

for _ in range(N):
    B.append([int(_) for _ in str(input()) if _!='\n'])

ans=0

def change(i, j, A):
    for a in range(3):
        for b in range(3):
            A[i+a][j+b]=A[i+a][j+b]^1

for i in range(0, len(A)-2):
    for j in range(0, len(A[0])-2):
        if A[i][j]!=B[i][j]:
            change(i, j, A)
            ans+=1
A="".join("".join(map(str, A[i]))for i in range(len(A)))
B="".join("".join(map(str, B[i]))for i in range(len(B)))
if A==B:
    print(ans)
else:
    print(-1)