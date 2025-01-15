import sys
import heapq

input=sys.stdin.readline
card=[]

for i in range(int(input())):
    heapq.heappush(card, int(input()))
    
ans=0
while len(card) != 1:
    tmp1 = heapq.heappop(card)
    tmp2 = heapq.heappop(card)
    heapq.heappush(card, tmp1+tmp2)
    ans+=tmp1+tmp2

print(ans)