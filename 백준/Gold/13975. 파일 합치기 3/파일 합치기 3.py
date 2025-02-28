import sys
import heapq

input=sys.stdin.readline


for _ in range(int(input())):
    N=int(input())
    files=list(map(int, input().split()))
    heapq.heapify(files)
    ans=0
    while 1:
        tmp=heapq.heappop(files)+heapq.heappop(files)
        if not files:
            break
        heapq.heappush(files, tmp)
        ans+=tmp
    print(ans+tmp)