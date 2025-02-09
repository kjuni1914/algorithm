import sys

input=sys.stdin.readline

N, S, M=map(int, input().split())

nums=list(map(int, input().split()))

dp=[0]*(M+1)
dp[S]=1

for i in range(len(nums)):
    before=dp.copy()
    dp=[0]*(M+1)
    flag=False
    for j in range(len(dp)):
        if before[j]==1:
            if 0<=j-nums[i]<=M:
                dp[j-nums[i]]=1
                flag=True
            if 0<=j+nums[i]<=M:
                dp[j+nums[i]]=1
                flag=True
    if flag==False:
        print(-1)
        sys.exit()

print(len(dp)-1-dp[::-1].index(1))