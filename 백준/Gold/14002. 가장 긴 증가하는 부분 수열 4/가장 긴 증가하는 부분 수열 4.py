import sys
input=sys.stdin.readline
N=int(input())
nums=list(map(int, input().split()))
dp=[1]*N
path=[[str(nums[i])] for i in range(N)]

for i in range(len(nums)):
    for j in range(i):
        if nums[j]<nums[i]:
            if dp[i]<dp[j]+1:
                dp[i]=dp[j]+1
                path[i]=path[j][:]
                path[i].append(str(nums[i]))

idx=dp.index(max(dp))
print(dp[idx])
print(" ".join(path[idx]))