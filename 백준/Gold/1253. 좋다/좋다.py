import sys

input=sys.stdin.readline
N=int(input())

nums=list(map(int, input().split()))
nums.sort()

def twoPnt(idx):
    l=0
    r=N-1
    target=nums[idx]
    while 1:
        if l==idx:
            l+=1
        if r==idx:
            r-=1
        if l>=r:
            return False
        s=nums[l]+nums[r]
        if s==target:
            return True
        elif s<target:
            l+=1
        else:
            r-=1

ans=0
for i in range(N):
    if twoPnt(i):
        ans+=1

print(ans)