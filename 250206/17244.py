import sys
from collections import deque

input=sys.stdin.readline

N, M=map(int, input().split())
house=[]

product=0
for i in range(M):
    tmp=input()
    tmp2=[]
    for j in range(N):
        if tmp[j]=="S":
            sti, stj=i, j
        if tmp[j]=="X":
            tmp2.append(2**product)
            product+=1
            continue
        tmp2.append(tmp[j])
    house.append(tmp2)

def bfs(i, j):
    visited=[[[-1 for i in range(N)] for j in range(M)] for k in range(2**(product))]
    collect=0
    visited[collect][i][j]=0
    queue=deque([(collect, i, j)])
    res=[]
    while queue:
        nowcollect, nowi, nowj=queue.popleft()
        tmp=visited[nowcollect][nowi][nowj]
        for di, dj in zip([0, 0, -1, 1], [1, -1, 0, 0]):
            if (0<=nowi+di<M and 0<=nowj+dj<N) and visited[nowcollect][nowi+di][nowj+dj]==-1 and house[nowi+di][nowj+dj]!="#":
                if isinstance(house[nowi+di][nowj+dj], int) and not (nowcollect&house[nowi+di][nowj+dj]):
                    nowcollect+=house[nowi+di][nowj+dj]
                    visited[nowcollect][nowi+di][nowj+dj]=tmp+1
                    queue.append((nowcollect, nowi+di, nowj+dj))
                    break
                else:
                    visited[nowcollect][nowi+di][nowj+dj]=tmp+1
                    queue.append((nowcollect, nowi+di, nowj+dj))

                if house[nowi+di][nowj+dj]=="E":
                    if nowcollect==2**(product)-1:
                        res.append(tmp+1)

    return res

print(min(bfs(sti, stj)))