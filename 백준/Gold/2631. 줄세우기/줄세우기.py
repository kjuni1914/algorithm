import sys

input=sys.stdin.readline
N=int(input())
dp=[0]*(N+1)
for _ in range(N):
    i=int(input())
    dp[i]=max(dp[:i])+1

print(N-max(dp))