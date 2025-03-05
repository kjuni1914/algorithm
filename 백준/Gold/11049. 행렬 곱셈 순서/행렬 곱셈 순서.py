import sys
inf=sys.maxsize

input=sys.stdin.readline

N=int(input())

dimention=[]

for _ in range(N):
    a, b=map(int, input().split())
    dimention.append([a, b])

dp=[[inf for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[i][i]=0

for length in range(1, N+1):
    for i in range(N-length+1):
        j=i+length-1
        for k in range(i, j):
            dp[i][j]=min(dimention[i][0]*dimention[k][1]*dimention[j][1]+dp[i][k]+dp[k+1][j], dp[i][j])

print(dp[0][N-1])