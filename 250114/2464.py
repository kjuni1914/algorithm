import copy
import sys

input=sys.stdin.readline

land = []
h = 0

for i in range(int(input())):
    tmp = list(map(int, input().split(" ")))
    land.append(tmp)
    if h < max(tmp):
        h = max(tmp)


def search(land, i, j, k, marker, res=0):
    check=[(1,0), (-1,0), (0,1), (0,-1)]
    if land[i][j]>k:
        for d in check:
            tmpi, tmpj = i+d[0], j+d[1]
            if 0<=tmpi<len(land) and 0<=tmpj<len(land[0]) and marker[tmpi][tmpj] == 0:
                marker[tmpi][tmpj] = 1
                res+=1
                res+=search(land, tmpi, tmpj, k, marker, res)

    return res


marker=[[0 for i in range(len(land[0]))] for j in range(len(land))]

print(search(land, 0, 0, 5, marker))