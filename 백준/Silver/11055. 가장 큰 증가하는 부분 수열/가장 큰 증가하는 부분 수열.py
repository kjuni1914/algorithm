import sys

input=sys.stdin.readline

N=int(input())

nums=list(map(int, input().split()))
dp=[0]*(max(nums)+1)
res=0

for i in range(N):
    dp[nums[i]]=max(dp[:nums[i]])+nums[i]
    if res<dp[nums[i]]:
        res=dp[nums[i]]
print(res)