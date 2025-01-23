import sys
from collections import deque

input=sys.stdin.readline

N=int(input())
pos=[0, 1, 2]
res=[0, 0, 0]
costs=[]
for i in range(N):
    costs.append(list(map(int, input().split(" "))))
i=0

for cost in costs[::-1]:
    for p in pos:
        if cost[(p+2)%3]>cost[(p+1)%3]:
            res[]
            p=(p+1)%3
        elif cost[(p+2)%3]<cost[(p+1)%3]:
            p=(p+2)%3

# print(now)