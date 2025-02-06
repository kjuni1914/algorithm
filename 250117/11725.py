import sys
sys.setrecursionlimit(10**6)

input=sys.stdin.readline
N=int(input())
graph={i+1:[] for i in range(N)}

for _ in range(N-1):
    i, j=map(int, input().split(" "))
    graph[i].append(j)
    graph[j].append(i)

visited=[0] * (N+1)
visited[1]=-1

def dfs(graph, stNode, visited):
    queue=[stNode]
    while queue:
        tmp=queue.pop()
        for i in graph[tmp]:
            if visited[i]==0:
                queue.append(i)
                visited[i]=tmp

dfs(graph, 1, visited)

for i in range(1, len(visited)):
    if i==0 or i==1:continue
    print(visited[i])