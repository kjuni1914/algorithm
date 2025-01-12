import sys
from collections import deque
input = sys.stdin.readline

cmd = list(map(int, input().split(" ")))

nearGraph = {i+1: [] for i in range(cmd[0])}
graph = {i+1: set() for i in range(cmd[0])}

answer=set()

for i in range(cmd[1]):
    tmp = list(map(int, input().split(" ")))
    nearGraph[tmp[0]].append(tmp[1])
    nearGraph[tmp[1]].append(tmp[0])


def bfs(nearGraph, stNode):
    if stNode not in graph[stNode]:
        search = deque()
        search.append(stNode)
        checker=set()
        checker.add(stNode)
        res=[stNode]
        while search:
            tmp = search.popleft()
            for i in sorted(nearGraph[tmp]):
                if i not in checker:
                    checker.add(i)
                    search.append(i)
                    res.append(i)
        for i in res:
            graph[i]=checker
        answer.add(tuple(checker))

for i in graph:
    bfs(nearGraph, i)

print(len(answer))