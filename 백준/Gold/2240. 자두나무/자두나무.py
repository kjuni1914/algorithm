import sys

input=sys.stdin.readline
T, W=map(int, input().split())

dp=[[0 for _ in range(W+1)] for _ in range(T+1)]
for i in range(1, T+1):
    fall=int(input())
    if fall==1:
        dp[i][0]=dp[i-1][0]+1
    else:
        dp[i][0]=dp[i-1][0]

    for j in range(1, W+1):
        if (fall==2 and j%2==0) or (fall==1 and j%2==1):
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]+1)
        else:
            dp[i][j]=dp[i-1][j]+1

print(max(dp[-1]))