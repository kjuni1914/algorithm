import sys
import heapq

input=sys.stdin.readline

N, K=map(int, input().split(" "))
jewels=[]
bags=[]

res=0

for _ in range(N):
    w, v=map(int, input().split(" "))
    heapq.heappush(jewels, (w, -v))

for _ in range(K):
    heapq.heappush(bags, int(input()))

candidate=[(0, 0)]
checker=1

while bags:
    bag=heapq.heappop(bags)
    while jewels and checker<=bag:
        w, v=heapq.heappop(jewels)
        if w<=bag:
            heapq.heappush(candidate, (v, w))
        else:
            heapq.heappush(jewels, (w, v))
            break
    checker=bag
    if candidate:
        res+=-heapq.heappop(candidate)[0]

print(res)