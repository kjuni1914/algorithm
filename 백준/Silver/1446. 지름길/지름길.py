import sys

input=sys.stdin.readline
N, D=map(int, input().split())

line=[]

for _ in range(N):
    line.append(list(map(int, input().split())))

dp=[0]+[None]*D
for j in range(1, D+1):
    dp[j]=dp[j-1]+1
    for i in line:
        if i[1]==j:
            dp[j]=min(dp[j], dp[i[0]]+i[2])

print(dp[D])