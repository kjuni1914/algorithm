import sys

input=sys.stdin.readline

N=int(input())
nums=list(map(str, input().split()))
l=max(len(i) for i in nums)
nums=list(map(lambda x:x*l, nums))

nums.sort(key=lambda x:x)
nums=list(map(lambda x:x[:int(len(x)/l)], nums))

if max(list(map(int, nums)))==0:
    print(0)
else:
    print("".join(nums[::-1]))