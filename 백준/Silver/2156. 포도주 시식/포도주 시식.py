import sys

input=sys.stdin.readline
N=int(input())
dp=[0, 0, 0]

for i in range(N):
    now=int(input())
    dp=(max(dp), dp[0]+now, dp[1]+now)

print(max(dp))