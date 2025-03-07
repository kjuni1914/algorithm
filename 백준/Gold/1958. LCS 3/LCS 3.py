import sys

input=sys.stdin.readline

A=input().rstrip()
B=input().rstrip()
C=input().rstrip()

a=len(A)+1
b=len(B)+1
c=len(C)+1

lcs=[[[0 for _ in range(c)] for _ in range(b)] for _ in range(a)]

for i in range(1, a):
    for j in range(1, b):
        for k in range(1, c):
            if A[i-1]==B[j-1]==C[k-1]:
                lcs[i][j][k]=lcs[i-1][j-1][k-1]+1
            else:
                lcs[i][j][k]=max(lcs[i-1][j][k], lcs[i][j-1][k], lcs[i][j][k-1])


print(lcs[a-1][b-1][c-1])