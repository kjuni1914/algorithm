import sys
input=sys.stdin.readline

N, M=map(int, input().split())
matrix=[list(map(int, input().split())) for _ in range(N)]


for _ in range(M):
    x1, y1, x2, y2=map(int, input().split())

    for i in range(x1-1, x2):
        if i==x1-1:
            res=matrix[x1-1][y1-1:y2]
        else:
            for j in range(y1-1, y2):
                res[j-y1+1]+=matrix[i][j]
                
    print(sum(res))