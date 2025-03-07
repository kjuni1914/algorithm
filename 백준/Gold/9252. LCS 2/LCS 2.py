import sys

input=sys.stdin.readline

A=input().rstrip()
B=input().rstrip()

a=len(A)+1
b=len(B)+1

lcs=[[0]*b for _ in range(a)]

for i in range(1, a):
    for j in range(1, b):
        if A[i-1]==B[j-1]:
            lcs[i][j]=lcs[i-1][j-1]+1
        else:
            lcs[i][j]=max(lcs[i-1][j], lcs[i][j-1])

res=[]
i, j=a-1, b-1
while i>0 and j>0:
    if A[i-1]==B[j-1]:
        res.append(A[i-1])
        i-=1
        j-=1
    else:
        if lcs[i-1][j]>lcs[i][j-1]:
            i-=1
        else:
            j-=1

if lcs[a-1][b-1]:
    print(lcs[a-1][b-1])
    char=""
    for i in res[::-1]:
        char+=i
    print(char)
else:
    print(0)