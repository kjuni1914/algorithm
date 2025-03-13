import sys

input=sys.stdin.readline

N=int(input())

dp=[1, 2, 3, 4, 5, 6]+[0]*(N-6)

if N<=6:
    print(N)
else:
    for i in range(6, N):
        dp[i]=max(dp[i-5]*4, dp[i-4]*3, dp[i-3]*2)
    print(dp[N-1])