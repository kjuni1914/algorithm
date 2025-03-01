import sys

input=sys.stdin.readline

for _ in range(int(input())):
    N=int(input())
    coins=list(map(int, input().split()))
    M=int(input())
    dp=[0]*(M+1)
    for i in range(N):
        if i==0:
            for j in range(1, M+1):
                if j%coins[i]==0:
                    dp[j]=1
        else:
            if M>=coins[i]: dp[coins[i]]+=1
            for j in range(coins[i]+1, M+1):
                if dp[j-coins[i]]:
                    dp[j]+=dp[j-coins[i]]
    print(dp[M])