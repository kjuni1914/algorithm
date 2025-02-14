import sys
input=sys.stdin.readline

N, K=map(int, input().split())

dp=[1]*(N+1)


for i in range(1, K):
    tmp=[0]*(N+1)
    for j in range(N+1):
        tmpsum=sum(dp[:j+1])
        tmp[j]=tmpsum
    dp=tmp

print(dp[N]%1000000000)