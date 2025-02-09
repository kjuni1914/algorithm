import sys
import heapq

input=sys.stdin.readline

N, M=map(int, input().split())

nums=list(map(int, input().split()))

heapq.heapify(nums)

for i in range(M):
    tmp=heapq.heappop(nums)+heapq.heappop(nums)
    heapq.heappush(nums, tmp)
    heapq.heappush(nums, tmp)

print(sum(nums))