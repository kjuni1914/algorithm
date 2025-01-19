import sys
input=sys.stdin.readline

N, M=map(int, input().split(" "))
coin=[]

for i in range(N):
    coin.append(int(input()))

dp=[[0 for _ in range(M+1)] for _ in range(N)]
ans=[-1]

for i in range(len(coin)):
    for j in range(M+1):
        if i==0:
            dp[i][j]=j//coin[i]
        else:
            if j>=coin[i]:
                dp[i][j]=min(dp[i-1][j-coin[i]]+coin[i], dp[i][j-coin[i]]+1)

print(dp)