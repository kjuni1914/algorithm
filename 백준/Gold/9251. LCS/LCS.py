import sys

input=sys.stdin.readline

A=input().rstrip(); B=input().rstrip()
a, b=len(A)+1, len(B)+1
lcs=[[0]*b for _ in range(a)]

for i in range(1, a):
    for j in range(1, b):
        if A[i-1]==B[j-1]:
            lcs[i][j]=lcs[i-1][j-1]+1
        else:
            lcs[i][j]=max(lcs[i-1][j], lcs[i][j-1])

print(lcs[a-1][b-1])