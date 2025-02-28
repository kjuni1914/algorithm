import sys

input=sys.stdin.readline

N, M=map(int, input().split())

field=[]

for _ in range(N):
    field.append(list(map(int, input().split())))

dp=[[0]*(M+1) for _ in range(N+1)]

for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        dp[i][j]=max(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])+field[i][j]

print(dp[0][0])