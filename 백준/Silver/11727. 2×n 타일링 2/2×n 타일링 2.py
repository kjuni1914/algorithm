import sys

input=sys.stdin.readline

N=int(input())

dp=[0]*max(N, 3)
dp[0]=1
dp[1]=3
dp[2]=5

for i in range(2, N):
    dp[i]=(dp[i-1]+dp[i-2]*2)%10007

print(dp[N-1])