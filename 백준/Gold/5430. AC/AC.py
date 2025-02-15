import sys

inpu=sys.stdin.readline

for _ in range(int(input())):
    cmd=input().strip()
    N=int(input())
    nums=eval(input().strip())
    if cmd.count("D")>len(nums):
        print("error")
        continue
    rev=False
    st=0
    end=len(nums)
    for i in cmd:
        if i=="R":
            rev= not rev
        if i=="D":
            if rev:
                end-=1
            else:
                st+=1
    else:
        
        if rev:
            print("["+",".join([str(i) for i in reversed(nums[st:end])])+"]")
        else:
            print("["+",".join([str(i) for i in nums[st:end]])+"]")
