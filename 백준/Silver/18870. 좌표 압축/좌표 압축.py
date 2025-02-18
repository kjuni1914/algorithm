import sys
input=sys.stdin.readline

N=int(input())

nums=list(map(int, input().split()))

idxnums={}
idx=0
for i in sorted(nums):
    if i not in idxnums:
        idxnums[i]=idx
        idx+=1

print(" ".join([str(idxnums[nums[i]]) for i in range(len(nums))]))