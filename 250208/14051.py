import sys

input=sys.stdin.readline

N=int(input())
dp=[0]*(21)

for i in range(1, N+1):
    t, p=map(int, input().split())
    if max(dp[:i])+p>dp[t+i-1]:
        dp[t+i-1]=max(dp[:i])+p

print(dp)
print(max(dp[:N+1]))