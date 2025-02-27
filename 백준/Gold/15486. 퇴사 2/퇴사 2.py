import sys

input=sys.stdin.readline
N=int(input())
dp=[0]*(N+1)

for i in range(N):
    day, rev=map(int, input().split())
    if i+day<N+1 and dp[i]+rev>dp[i+day]:
        dp[i+day]=dp[i]+rev
    if dp[i]>dp[i+1]:
        dp[i+1]=dp[i]

print(dp[N])