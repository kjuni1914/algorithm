import sys
import heapq

input=sys.stdin.readline
N=int(input())
inf=sys.maxsize

state=[]
for _ in range(N):
    state.append(input().rstrip())

graph=[]
for i in range(N):
    graph.append([])
    for j in range(N):
        if i==j:
            continue
        tmp=0
        for x, y in zip(state[i], state[j]):
            tmp+=(int(x)-int(y))**2
        graph[i].append((j, tmp))

now, obj=map(int, input().split())
now-=1; obj-=1

def dijkstra(node):
    res=[inf]*N
    res[node]=0
    queue=[(0, node)]
    while queue:
        noww, now=heapq.heappop(queue)
        if noww>res[now]:
            continue
        for nxt, nxtw in graph[now]:
            if noww+nxtw<res[nxt]:
                res[nxt]=noww+nxtw
                heapq.heappush(queue, (noww+nxtw, nxt))
    return res

print(dijkstra(now)[obj])