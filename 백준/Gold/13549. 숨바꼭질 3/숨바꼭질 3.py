import sys
from collections import deque

input = sys.stdin.readline

cmd1, cmd2 = map(int, input().split(" "))

def teleport(position: deque, endPoint, visited): # deque로 현재 포지션을 받아서 2의 멱승꼴 ~ endpoint+1까지 다 집어넣기
    for _ in range(len(position)):
        tmp = position.popleft()
        i=0
        if 0 < tmp <= endPoint+1:
            while tmp*(2**i)<=endPoint+1:
                position.append(tmp*(2**i))
                visited[tmp*(2**i)]=True
                i+=1
        else:
            position.append(tmp)

def bfs(stPoint, endPoint):
    visited = [False] * 200001

    search = deque([stPoint])
    res=0
    while search:
        teleport(search, endPoint, visited)

        if visited[endPoint]==True:
            return res
        
        for _ in range(len(search)):
            tmp = search.popleft()
            for i in [tmp+1, tmp-1]:
                if 0<=i<=100000 and visited[i] == False:
                    search.append(i)
                    visited[i]=True
        res+=1
        
print(bfs(cmd1, cmd2))