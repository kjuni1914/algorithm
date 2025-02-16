import sys

input=sys.stdin.readline

for _ in range(int(input())):
    calls=set()
    flag=False
    bound=0
    nums=[]
    for _ in range(int(input())):
        nums.append(input().strip())
    nums.sort()
    for num in nums:
        for i in range(bound):
            if num[:i+1] in calls:
                flag=True
                break
        else:
            calls.add(num)
            if bound<len(num):
                bound=len(num)
    if flag==True:
        print("NO")
    else:
        print("YES")