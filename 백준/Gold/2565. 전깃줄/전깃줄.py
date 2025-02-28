import sys

input=sys.stdin.readline

N=int(input())

lines=[]

for _ in range(N):
    lines.append(list(map(int, input().split())))

dp=[0]*(max([max(lines[i]) for i in range(N)])+1)

lines.sort()

for i in range(len(lines)):
    dp[lines[i][1]]=max(dp[:lines[i][1]])+1

print(N-max(dp))