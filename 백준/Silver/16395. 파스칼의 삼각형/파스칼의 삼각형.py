import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp=[[1]*i for i in range(1, N+1)]

for i in range(2, N):
    for j in range(1, i):
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j]

print(dp[N-1][K-1])