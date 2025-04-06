import sys
input=sys.stdin.readline
N,M,K=map(int,input().split())
if K==0:
    dp=[[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i==0 or j==0:
                dp[i][j]=1
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
    print(dp[-1][-1])
else:
    r=(K-1)//M
    c=(K-1)%M
    dp1=[[0]*(c+1) for _ in range(r+1)]
    for i in range(r+1):
        for j in range(c+1):
            if i==0 or j==0:
                dp1[i][j]=1
            else:
                dp1[i][j]=dp1[i-1][j]+dp1[i][j-1]
    dp2=[[0]*(M-c) for _ in range(N-r)]
    for i in range(N-r):
        for j in range(M-c):
            if i==0 or j==0:
                dp2[i][j]=1
            else:
                dp2[i][j]=dp2[i-1][j]+dp2[i][j-1]

    print(dp1[-1][-1]*dp2[-1][-1])
