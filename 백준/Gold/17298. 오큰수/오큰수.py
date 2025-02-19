import sys
input=sys.stdin.readline

N=int(input())
nums=list(map(int, input().split()))

dp=[-1]*(N)
dp[N-1]=-1

for i in range(N-2, -1, -1):
    if nums[i]<nums[i+1]:
        dp[i]=i+1
    else:
        next=i+1
        while next!=-1 and nums[i]>=nums[next]:
            next=dp[next]
        dp[i]=next

print(" ".join([str(nums[i]) if i!=-1 else "-1" for i in dp]))