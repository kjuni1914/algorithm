import sys

input=sys.stdin.readline

N=int(input())
pack=list(map(int, input().split()))
dp=[0]+[float('inf')]*(N)

for i in range(N):
    amount=i+1
    for j in range(1, N+1):
        if j>=amount:
            if dp[j-amount]+pack[i]<dp[j]:
                dp[j]=dp[j-amount]+pack[i]

print(dp[N])