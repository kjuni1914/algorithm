import sys
from collections import deque

input=sys.stdin.readline
N=int(input())


build=[0]*(N+1)
prebuild=[set() for _ in range(N+1)]
degree=[0]*(N+1)

for i in range(1, N+1):
    cmd=list(map(int, input().rstrip().split()))
    build[i]=cmd[0]
    for j in range(1, len(cmd)-1):
        prebuild[cmd[j]].add(i)
        degree[i]+=1

queue=deque()

for i in range(1, N+1):
    if degree[i]==0:
        queue.append(i)

res=build[:]

while queue:
    time=0

    for _ in range(len(queue)):
        now=queue.popleft()
        for i in prebuild[now]:
            degree[i]-=1
            res[i]=max(res[i], res[now]+build[i])
            if degree[i]==0:
                queue.append(i)

for i in range(1, len(res)):
    print(res[i])