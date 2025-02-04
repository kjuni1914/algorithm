import sys

input=sys.stdin.readline

for _ in range(int(input())):
    tmp1=[]
    tmp2=[]
    length=int(input())
    nums=list(map(int, input().split()))
    nums.sort()
    flag=True
    for i in nums:
        if flag:
            tmp1.append(i)
            flag=False
        else:
            tmp2.append(i)
            flag=True
    tmp1.extend(tmp2[::-1])

    print(max([abs(tmp1[i]-tmp1[i-1]) for i in range(length)]))