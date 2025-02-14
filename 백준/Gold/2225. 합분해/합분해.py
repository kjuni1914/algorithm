import sys

N, K=map(int, input().split())

dp=[[1]*(N+1)]
for _ in range(K-1):
    dp.append([0]*(N+1))


for i in range(1, K):
    for j in range(N+1):
        tmp=0
        for k in range(j+1):
            tmp+=dp[i-1][k]*dp[0][j-k]
        dp[i][j]=tmp


print(dp[K-1][N]%1000000000)