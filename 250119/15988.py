import sys
input=sys.stdin.readline

N=int(input())
num=[]

for _ in range(N):
    num.append(int(input()))

dp=[0]*(max(num)+1)
dp[1]=1
dp[2]=2
dp[3]=4

for i in range(4, max(num)+1):
    dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1000000009

for i in num:
    print(dp[i])