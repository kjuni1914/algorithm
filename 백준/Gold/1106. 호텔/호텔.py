import sys

input=sys.stdin.readline
C, N=map(int, input().split())

dp=[0]+[float('inf')]*(1100)

for i in range(N):
    c, r=map(int, input().split())
    for j in range(r, 1101):
        dp[j]=min(dp[j-r]+c, dp[j])

print(min(dp[C:]))