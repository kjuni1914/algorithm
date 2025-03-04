import sys

input=sys.stdin.readline

for _ in range(int(input())):
    N=int(input())
    cost=list(map(int, input().split()))
    psum=[0]*(N+1)
    for i in range(N):
        psum[i+1]=psum[i]+cost[i]
    dp = [[0] * N for _ in range(N)]
    for length in range(2, N+1):
        for i in range(N-length+1):
            j=i+length-1
            tmpmin=float('inf')
            for k in range(i, j):
                if tmpmin>dp[i][k]+dp[k+1][j]:
                    tmpmin=dp[i][k]+dp[k+1][j]
            dp[i][j]+=psum[j+1]-psum[i]+tmpmin

    print(dp[0][N-1])