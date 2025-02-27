import sys
input=sys.stdin.readline
N=int(input())


nums=list(map(int, input().split()))
nums.reverse()
dp=[0]*(max(nums)+1)

for i in range(len(nums)):
    dp[nums[i]]=max(dp[:nums[i]])+1

print(max(dp))