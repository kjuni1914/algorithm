import sys
from collections import deque

input=sys.stdin.readline
N, M=map(int, input().split())
rank=[0]*N
graph=[[] for _ in range(N)]

for _ in range(M):
    pre, next=map(int, input().split())
    graph[pre-1].append(next-1)
    rank[next-1]+=1

ans=[0 for _ in range(N)]
queue=deque()

for i in range(len(rank)):
    if rank[i]==0:
        queue.append(i)
        ans[i]=str(1)        

cnt=1

while queue:
    cnt+=1
    for _ in range(len(queue)):
        tmp=queue.popleft()
        for i in graph[tmp]:
            rank[i]-=1
            if rank[i]==0:
                queue.append(i)
                ans[i]=str(cnt)

print(" ".join(ans))