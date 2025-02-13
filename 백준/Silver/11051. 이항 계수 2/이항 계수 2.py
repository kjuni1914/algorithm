import sys
input=sys.stdin.readline

N, K=map(int, input().split())

dp=[0]*N+[1]

for i in range(N+1):
    for j in range(N-i, N):
        dp[j]=dp[j+1]+dp[j]

print(dp[K]%10007)