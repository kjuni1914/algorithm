import sys
import heapq

input = sys.stdin.readline

cmd1, cmd2 = map(int, input().split(" "))
graph = {i+1:[0 if i+1 == j else float("inf") for j in range(cmd1+1)] for i in range(cmd1)}
stNode = int(input())

for i in range(cmd2):
    st, end, cost = map(int, input().split(" "))
    graph[st][end] = cost

def dijkstra(graph, stNode):
    distance = [float("inf")] * (len(graph) + 1)
    distance[stNode] = 0
    queue=[]
    heapq.heappush(queue, [distance[stNode], stNode])

    while queue:
        nowDistance, nowNode = heapq.heappop(queue)

        if distance[nowNode] < nowDistance:
            continue
        
        for i in range(1, len(graph)+1):
            newDistance, newNode = graph[nowNode][i], i
            if newDistance != float("inf"):
                tmpDistance = newDistance + distance[nowNode]
                if tmpDistance < distance[newNode]:
                    distance[newNode] = tmpDistance
                    heapq.heappush(queue, [distance[newNode], newNode])

    return distance

for i, value in enumerate(dijkstra(graph, stNode)):
    if i==0:
        continue
    if i == "inf":
        print("INF")
    else:
        print(value)