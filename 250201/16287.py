import sys

input=sys.stdin.readline

w, n=map(int, input().split())
nums=list(map(int, input().split()))

mem=[False]*w

for i in range(n):
    for j in range(i+1, n):
        if nums[i]+nums[j]<w and mem[w-nums[i]-nums[j]]:
            print("YES")
            sys.exit()
    for j in range(i):
        if nums[i]+nums[j]<w:
            mem[nums[i]+nums[j]]=True

print("NO")