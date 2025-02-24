import sys
import heapq

input=sys.stdin.readline
N=int(input())
K=int(input())
if N<=K:
    print(0)
    sys.exit()
sensor=list(map(int, input().split()))

sensor.sort()
distance=[]
for i in range(N-1):
    heapq.heappush(distance, -(sensor[i+1]-sensor[i]))

for i in range(K-1):
    heapq.heappop(distance)

print(-sum(distance))