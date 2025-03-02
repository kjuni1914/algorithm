import sys

input=sys.stdin.readline
N, L=map(int, input().split())

hole=list(map(int, input().split()))

hole.sort()

now=0
ans=0
for i in hole:
    if now>=i+0.5:
        continue
    if now<=i-0.5:
        now=i+L-0.5
        ans+=1
    else:
        now+=L-0.5
        ans+=1

print(ans)