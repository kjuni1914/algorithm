import sys
import heapq

input=sys.stdin.readline

V, E=map(int, input().split())

st=int(input())-1
graph=[[] for _ in range(V)]

for _ in range(E):
    cmd=list(map(int, input().split()))
    graph[cmd[0]-1].append([cmd[1]-1, cmd[2]])

def dijkstra(st):
    res=[float('inf')]*V
    res[st]=0
    queue=[(0, st)]

    while queue:
        d, now=heapq.heappop(queue)
        if d>res[now]:
            continue
        for nxt, nd in graph[now]:
            if d+nd<res[nxt]:
                res[nxt]=d+nd
                heapq.heappush(queue, (res[nxt], nxt))
    return res

res=dijkstra(st)
for i in res:
    print(str.upper(str(i)))