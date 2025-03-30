import sys
input = sys.stdin.readline

N=int(input())
nums=list(map(int, input().split()))

dp1=[1]*N
dp2=[1]*N

for i in range(1, N):
    if nums[i]>=nums[i-1]:
        dp1[i]=dp1[i-1]+1
    if nums[i]<=nums[i-1]:
        dp2[i]=dp2[i-1]+1

print(max(max(dp1), max(dp2)))
