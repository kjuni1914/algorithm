import sys

input=sys.stdin.readline

R, C=map(int, input().split())
field=[]
for i in range(R):
    field.append(list(input().rstrip()))

used=[[-1]*C for _ in range(R)]

def dfs(x, y, used):
    if y==C-1:
        used[x][y]=1
        return 1
    used[x][y]=0
    for dx, dy in zip([-1, 0, 1], [1, 1, 1]):
        if 0<=x+dx<R and 0<=y+dy<C:
            if field[x+dx][y+dy]=="." and used[x+dx][y+dy]==-1:
                if dfs(x+dx, y+dy, used):
                    used[x][y]=1
                    return 1
    return 0

res=0
for i in range(R):
    res+=dfs(i, 0, used)
print(res)