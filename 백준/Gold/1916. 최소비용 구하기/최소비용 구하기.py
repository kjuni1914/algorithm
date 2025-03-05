import sys
import heapq

inf=sys.maxsize
input=sys.stdin.readline
N=int(input())
res=[inf]*(N+1)
graph=[[] for _ in range(N+1)]
M=int(input())

for _ in range(M):
    st, v, w=map(int, input().split())
    graph[st].append([v, w])

st, dest=map(int, input().split())
res[st]=0


def dijkstra(st):
    queue=[]
    heapq.heappush(queue, (0, st))
    while queue:
        tw, tv=heapq.heappop(queue)
        if tw>res[tv]:
            continue
        for v, w in graph[tv]:
            if tw+w<res[v]:
                res[v]=tw+w
                heapq.heappush(queue, (tw+w, v))

dijkstra(st)
print(res[dest])