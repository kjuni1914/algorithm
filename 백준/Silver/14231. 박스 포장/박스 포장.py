import sys

input=sys.stdin.readline

N=int(input())

box=list(map(int, input().split()))

dp=[0]*100001
res=0

for i in range(N):
    dp[box[i]]=max(dp[:box[i]])+1
    if res<dp[box[i]]:
        res=dp[box[i]]

print(res)