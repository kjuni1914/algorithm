import sys

input=sys.stdin.readline
using=[]

for i in range(int(input())):
    using.append(list(map(int, input().split(" "))))

using.sort(key=lambda x:(x[1], x[0]))

now=-1
ans=0

for i in using:
    if now<=i[0]:
        now=i[1]
        ans+=1

print(ans)