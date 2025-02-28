import sys
import math
input=sys.stdin.readline

N, L=map(int, input().split())

pools=[]
for _ in range(N):
    pools.append(list(map(int, input().split())))
pools.sort()

now=0
ans=0
for i in pools:
    if now<=i[0]:
        ans+=math.ceil((i[1]-i[0])/L)
        now=i[0]+math.ceil((i[1]-i[0])/L)*L
    else:
        ans+=math.ceil((i[1]-now)/L)
        now=now+math.ceil((i[1]-now)/L)*L

print(ans)