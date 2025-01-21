import sys
input=sys.stdin.readline

N, M=map(int, input().split(" "))
coin=[]

for i in range(N):
    coin.append(int(input()))
coin.sort()

dp=[0 for _ in range(M+1)]
pos=[False for _ in range(M+1)]

for i in range(len(coin)):
    for j in range(M+1):
        if j%coin[i]==0:
            if pos[j]==True:
                dp[j]=min(dp[j], j//coin[i])
            else:
                dp[j]=j//coin[i]
            pos[j]=True
        else:
            if j>=coin[i] and pos[j-coin[i]]==True:
                if pos[j]==True:
                    dp[j]=min(dp[j-coin[i]]+1, dp[j])
                else:
                    dp[j]=dp[j-coin[i]]+1
                pos[j]=True

print(dp[M] if pos[M]==True else -1)