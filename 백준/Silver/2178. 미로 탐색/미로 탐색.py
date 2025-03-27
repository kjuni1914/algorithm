import sys
from collections import deque

input=sys.stdin.readline
N, M=map(int, input().split())
field=[]

for _ in range(N):
    field.append(list(map(int, input().rstrip())))

def bfs():
    queue=deque([(0, 0)])
    visited=[[-1]*M for _ in range(N)]
    visited[0][0]=1

    while queue:
        nowx, nowy=queue.popleft()
        for dx, dy in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
            tmpx, tmpy=nowx+dx, nowy+dy
            if 0<=tmpx<N and 0<=tmpy<M and visited[tmpx][tmpy]==-1 and field[tmpx][tmpy]==1:
                queue.append((tmpx, tmpy))
                visited[tmpx][tmpy]=visited[nowx][nowy]+1
    return visited

print(bfs()[-1][-1])