import sys
from collections import deque

input=sys.stdin.readline
N=int(input())
works=[0]*N
graph=[[] for _ in range(N)]
rank=[0]*N
queue=deque()
visited=[False]*N

for i in range(N):
    cmd=list(map(int, input().split()))
    works[i]=cmd[0]
    rank[i]+=cmd[1]
    for j in cmd[2:]:
        graph[j-1].append(i)
    if rank[i]==0:
        queue.append(i)
        visited[i]=True

time=[0]*N

while queue:
    for _ in range(len(queue)):
        now=queue.popleft()
        time[now]+=works[now]
        for next in graph[now]:
            rank[next]-=1
            time[next]=max(time[next], time[now])
            if rank[next]==0:
                queue.append(next)


print(max(time))