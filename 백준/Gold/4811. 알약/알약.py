import sys

input=sys.stdin.readline

dp=[[0]*31 for _ in range(31)]
dp[0][0]=1
for i in range(31):
    for j in range(i+1):
        dp[i][j]+=dp[i-1][j]+dp[i][j-1]

while 1:
    N=int(input())
    if N==0:
        sys.exit()
    print(dp[N][N])