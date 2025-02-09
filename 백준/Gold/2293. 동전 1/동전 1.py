import sys

input=sys.stdin.readline

cmd1, cmd2 = map(int, input().split(" "))
coin=[]
dp = [0]*(cmd2+1)
dp[0]=1

for i in range(cmd1):
    coin.append(int(input()))

for i in range(len(coin)):
    for j in range(len(dp)):
        if j>=coin[i]:
            dp[j]=dp[j-coin[i]] + dp[j]

print(dp[cmd2])