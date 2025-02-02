import sys

input=sys.stdin.readline
N=int(input())
targets=list(map(int, input().split()))
M=int(input())
nums=list(map(int, input().split()))
targets.sort()

for i in nums:
    s=0
    e=len(targets)-1
    flag=False
    while s<=e:
        if targets[(s+e)//2]<i:
            s=(s+e)//2+1
        elif targets[(s+e)//2]>i:
            e=(s+e)//2-1
        else:
            print(1)
            break
    else:
        print(0)
