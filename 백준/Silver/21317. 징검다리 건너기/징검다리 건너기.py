import sys
input=sys.stdin.readline
inf=sys.maxsize

N=int(input())
cost=[]
for _ in range(N-1):
    cost.append(list(map(int, input().split())))

bbig=int(input())

dp=[[0]+[inf]*(N-1), [inf]*N]

for i in range(N-1):
    dp[0][i+1]=min(dp[0][i+1], dp[0][i]+cost[i][0])
    dp[1][i+1] = min(dp[1][i+1], dp[1][i] + cost[i][0])
    if i+2<N:
        dp[0][i+2]=min(dp[0][i+2], dp[0][i]+cost[i][1])
        dp[1][i+2] = min(dp[1][i+2], dp[1][i] + cost[i][1])
    if i+3<N:
        dp[1][i+3]=min(dp[1][i+3], dp[0][i]+bbig)

print(min(dp[0][N-1], dp[1][N-1]))