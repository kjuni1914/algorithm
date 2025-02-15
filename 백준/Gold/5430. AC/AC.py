import sys

inpu=sys.stdin.readline

for _ in range(int(input())):
    cmd=input().strip()
    N=int(input())
    nums=eval(input().strip())
    rnums=nums[::-1]
    if cmd.count("D")>len(nums):
        print("error")
        continue
    rev=False
    for i in cmd:
        if i=="R":
            rev= not rev
        if i=="D":
            if rev:
                nums.pop()
                rnums.pop(0)
            else:
                nums.pop(0)
                rnums.pop()
    else:
        if rev:
            print("["+",".join([str(i) for i in rnums])+"]")
        else:
            print("["+",".join([str(i) for i in nums])+"]")