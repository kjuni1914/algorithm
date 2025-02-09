import sys

input=sys.stdin.readline

N=int(input())

nums=list(map(int, input().split()))
dp=[0]*N

for i in range(N):
    dp[i]=max(nums[i], dp[i-1]+nums[i])
print(max(dp))