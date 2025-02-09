import sys
from collections import deque

input=sys.stdin.readline

cmd = list(map(int, input().split(" ")))

d = {(i+1): [] for i in range(cmd[0])}


for i in range(cmd[1]):
    tmp = list(map(int, input().split(" ")))
    d[tmp[0]].append(tmp[1])
    d[tmp[1]].append(tmp[0])

def dfs(d, node, l=None):
    l=l or [node]
    for i in sorted(d[node]):
        if i not in l:
            l.append(i)
            dfs(d, i, l)
    return l

def bfs(d, node):
    l=deque()
    l.append(node)
    s=set()
    s.add(node)
    res=[]
    res.append(node)
    while l:
        tmp = l.popleft()
        for i in sorted(d[tmp]):
            if i not in s:
                l.append(i)
                s.add(i)
                res.append(i)

    return res

print(" ".join(str(i) for i in dfs(d, cmd[2])))
print(" ".join(str(i) for i in bfs(d, cmd[2])))