import sys
import heapq

input=sys.stdin.readline

stick=[]
tmpmax=0
for i in range(int(input())):
    L, H=map(int, input().split())
    heapq.heappush(stick, (-H, L))
    if tmpmax<H: tmpmax=H

bound=(stick[0][1], stick[0][1])
ans=stick[0][0]
while stick:
    H, L=heapq.heappop(stick)
    if L<bound[0]:
        ans+=(bound[0]-L)*H
        bound=(L, bound[1])
    elif L>bound[1]:
        ans+=(L-bound[1])*H
        bound=(bound[0], L)

print(-ans)