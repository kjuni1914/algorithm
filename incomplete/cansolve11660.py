import sys
input=sys.stdin.readline

N, M=map(int, input().split())
matrix=[list(map(int, input().split())) for _ in range(N)]
memoization=set()
calValue={}

for _ in range(M):
    x1, y1, x2, y2=map(int, input().split())

    for i in range(x1-1, x2):
        if i==x1-1:
            res=matrix[x1-1][y1-1:y2]
        else:
            for j in range(y1-1, y2):
                if (i, j, x2-1, y2-1) in memoization:
                    res[j-y1+1]=calValue[(i, j, x2-1, y2-1)]
                else:
                    res[j-y1+1]+=matrix[i][j]
                    memoization.add((x1-1, y1-1, i, j))
                    calValue[(x1-1, y1-1, i, j)]=res[j-y1+1]

    print(sum(res))