import sys

input=sys.stdin.readline
N=int(input())

def check(num, cnt):
    for i in range(2, int(num**(1/2)+1)):
        if num%i==0:
            return
    if len(str(num))==N:
        print(num)
        return
    for j in nums:
        check(int(str(num)[:cnt]+j), cnt+1)

nums=[str(i+1) for i in range(9)]

for i in (2, 3, 5, 7):
    tmp=str(i)
    check(int(tmp), 1)
