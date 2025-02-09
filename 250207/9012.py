import sys

input=sys.stdin.readline

N=int(input())
for i in range(N):
    cmd=input().strip()
    stack=[]
    for i in cmd:
        if i=="(":
            stack.append(")")
        else:
            if stack and stack.pop()==i:
                continue
            else:
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")
        continue
    print("NO")
    