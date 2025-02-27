import sys

input=sys.stdin.readline
N=int(input())

if N==1:
    print(int(input()))
    sys.exit()

nums=list(map(int, input().split()))
dp=[[0]*N for _ in range(2)]

for i in range(N):
    dp[1][i]=max(dp[0][i-2], dp[1][i-1])+nums[i]
    if dp[0][i-1]+nums[i]>=nums[i]:
        dp[0][i]=dp[0][i-1]+nums[i]
    else:
        dp[0][i]=nums[i]
    
print(max(max(dp[0]), max(dp[1])))