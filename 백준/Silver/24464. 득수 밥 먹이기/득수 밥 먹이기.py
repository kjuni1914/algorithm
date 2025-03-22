import sys

input=sys.stdin.readline
N=int(input())
dp=[1, 1, 1, 1, 1]

for _ in range(1, N):
    dp=[sum(dp[1:])%1000000007, 
        (dp[0]+dp[3]+dp[4])%1000000007, 
        (dp[0]+dp[4])%1000000007, 
        (dp[0]+dp[1])%1000000007, 
        sum(dp[:3])%1000000007]

print(sum(dp)%1000000007)