import sys

input=sys.stdin.readline
N=int(input())

cnt=1
ans=[]
stack=[]
for _ in range(N):
    num=int(input())
    if num>=cnt:
        while cnt<=num:
            stack.append(cnt)
            ans.append('+')
            cnt+=1
        stack.pop()
        ans.append('-')
    else:
        if num==stack[-1]:
            stack.pop()
            ans.append('-')
        else:
            print('NO')
            sys.exit()

for i in ans:
    print(i)