import sys

input=sys.stdin.readline

N, C=map(int, input().split())
packages=[]

using=[C]*(N+1)

for _ in range(int(input())):
    s, e, w=map(int, input().split())
    packages.append((s, e, w))

packages.sort(key=lambda x:(x[1], x[0]))
ans=0

for i in packages:
    carry=min(i[2], min(using[i[0]:i[1]]))
    for j in range(i[0], i[1]):
        using[j]-=carry
    ans+=carry

print(ans)