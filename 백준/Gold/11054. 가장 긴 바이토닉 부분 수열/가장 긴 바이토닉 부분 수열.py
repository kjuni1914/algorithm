import sys
input=sys.stdin.readline

N=int(input())
nums=list(map(int, input().split()))
rnums=nums[::-1]

dp1=[0]*(max(nums)+2)
dp2=[0]*(max(nums)+2)
res=[0]*(N)
for i in range(len(nums)):
    dp1[nums[i]]=max(dp1[:nums[i]])+1
    res[i]+=dp1[nums[i]]

for i in range(len(nums)):
    dp2[rnums[i]]=max(dp2[:rnums[i]])+1
    res[N-1-i]+=dp2[rnums[i]]-1

print(max(res))