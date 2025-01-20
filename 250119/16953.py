import sys
input=sys.stdin.readline
from collections import deque

N, M=map(int, input().split(" "))
MAX=M
queue=deque([N])
visited=set()
visited.add(N)

res=0
flag=True
while queue:
    for i in range(len(queue)):
        tmp=queue.popleft()
        for next in tmp*2, tmp*10+1:
            if 1<=next<=MAX and next not in visited:
                visited.add(next)
                queue.append(next)
    res+=1
    if M in visited:
        print(res+1)
        flag=False
        break
if flag:
    print(-1)