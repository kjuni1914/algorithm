import sys
input=sys.stdin.readline

N=int(input())
nums=list(map(int, input().split()))
dp=[0]*(max(nums)+1)
for i in nums:
    dp[i]=max(dp[:i])+1
print(max(dp))