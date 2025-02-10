import sys

input=sys.stdin.readline

N=int(input())

tmp=list(map(int, input().split()))
pack={i+1:tmp[i] for i in range(N)}
dp=[0]*(N+1)

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i]=max(dp[i-j]+pack[j], dp[i])

print(dp[N])