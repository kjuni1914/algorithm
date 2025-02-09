import sys
from collections import deque

input=sys.stdin.readline

cmd=input().strip()

table=[[0 for _ in range(len(cmd))] for _ in range(len(cmd))]

for i in range(len(cmd)):
    for j in range(i, len(cmd)):
        if cmd[i:j+1]==cmd[i:j+1][::-1]:
            table[i][j]=1

nowi=0
stack=deque()

for i in range(len(table[0])):
    if table[0][i]==1:
        stack.append([i, 1])

res=[]
dp=[float('inf')]*len(cmd)

while stack:
    tmp=stack.popleft()
    if tmp[0]!=len(cmd)-1:
        for i in range(tmp[0], len(table[tmp[0]+1])):
            if table[tmp[0]+1][i]==1 and dp[i]>tmp[1]+1:
                stack.append([i, tmp[1]+1])
                dp[i]=tmp[1]+1
    else:
        res.append(tmp[1])

print(min(res)) 