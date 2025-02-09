import sys
import copy
from collections import deque

def bfs(stNode, endPnt):
    search = deque([stNode])
    visted = set([stNode])
    res=0
    while search: 
        for _ in range(len(search)):
            tmp = search.popleft()
            if tmp == endPnt:
                return res
            for i in tmp-1, tmp+1, tmp*2:
                if i not in visted and 0<=i<=100000:
                    search.append(i)
                    visted.add(i)
        res+=1

input = sys.stdin.readline

cmd1, cmd2 = map(int, input().split(" "))

print(bfs(cmd1, cmd2))