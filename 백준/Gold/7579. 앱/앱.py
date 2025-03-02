import sys

input=sys.stdin.readline
N, M=map(int, input().split())

A=list(map(int, input().split()))
c=list(map(int, input().split()))

dp=[0]*(sum(c)+1)

for i in range(N):
    tmp=dp[:]
    for j in range(sum(c)+1):
        if j>=c[i]:
            dp[j]=max(tmp[j-c[i]]+A[i], dp[j])

for i in range(sum(c)+1):
    if dp[i]>=M:
        print(i)
        break