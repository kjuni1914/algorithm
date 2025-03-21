import sys

input=sys.stdin.readline

n, m=map(int, input().split())
dp=[[0]*m for _ in range(n)]

field=[]
res=0
for i in range(n):
    field.append(list(map(int, list(input().rstrip()))))
for i in range(n):
    for j in range(m):
        if field[i][j]==1:
            dp[i][j]=min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
            if dp[i][j]>res:
                res=dp[i][j]

print(res**2)