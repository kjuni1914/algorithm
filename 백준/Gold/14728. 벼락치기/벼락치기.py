import sys

input=sys.stdin.readline

N, T=map(int, input().split())

dp=[0]*(T+1)
for _ in range(N):
    K, S=map(int, input().split())
    if T<K:
        continue
    tmp=dp[:]
    for j in range(K, T+1):
        dp[j]=max(tmp[j-K]+S, tmp[j])

print(dp[T])