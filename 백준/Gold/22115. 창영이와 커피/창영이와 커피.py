import sys

input=sys.stdin.readline
N, K=map(int, input().split())

if K==0:
    print(0)
    sys.exit()

dp=[N+1]*(K+1)
caffeine=list(map(int, input().split()))

for i in range(N):
    if caffeine[i]>K:
        continue
    dp[caffeine[i]]=1
    tmp=dp[:]
    for j in range(caffeine[i]+1, K+1):
        dp[j]=min(tmp[j-caffeine[i]]+1, dp[j])


print(dp[K] if dp[K]<=N else -1)