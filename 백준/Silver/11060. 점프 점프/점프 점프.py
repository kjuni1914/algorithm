import sys
inf=sys.maxsize
input=sys.stdin.readline

N=int(input())

dp=[0]+[inf]*(N-1)

jump=list(map(int, input().split()))
for i in range(N):
    for j in range(1, jump[i]+1):
        if i+j<N:
            dp[i+j]=min(dp[i+j], dp[i]+1)

if dp[N-1]==inf:
    print(-1)
else:
    print(dp[N-1])