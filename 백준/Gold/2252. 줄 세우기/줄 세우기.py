import sys
from collections import deque

input=sys.stdin.readline
N, M=map(int, input().split())

graph=[[] for _ in range(N)]
rank=[0]*N

for _ in range(M):
    pre, nxt=map(int, input().split())
    pre-=1
    nxt-=1

    graph[pre].append(nxt)
    rank[nxt]+=1

queue=deque()

for i in range(N):
    if rank[i]==0:
        queue.append(i)

while queue:
    now=queue.popleft()
    print(now+1, end=" ")
    for i in graph[now]:
        rank[i]-=1
        if rank[i]==0:
            queue.append(i)