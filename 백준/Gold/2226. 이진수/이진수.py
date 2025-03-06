import sys

input=sys.stdin.readline

N=int(input())
dp=[0]*(N)
for i in range(1, N):
    if i%2==1:
        dp[i]=dp[i-1]*2+1
    else:
        dp[i]=dp[i-1]*2-1

print(dp[N-1])