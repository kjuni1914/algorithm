import sys

input=sys.stdin.readline

N=int(input())
dp=[1]*10
for i in range(1, N):
    tmp=dp[:]
    for j in range(10):
        tmp[j]=sum(dp[:j+1])
    dp=tmp

print(sum(dp)%10007)