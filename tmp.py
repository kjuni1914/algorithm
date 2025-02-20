import sys

input=sys.stdin.readline

nums=[]
N=int(input())
for _ in range(N):
    nums.extend(list(map(int, input().split())))
    nums.sort(reverse=True)
    nums=nums[:N]

print(nums[N-1])