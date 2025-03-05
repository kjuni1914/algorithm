import sys

input=sys.stdin.readline
N=int(input())

weights=list(map(int, input().split()))

dp=[False]*(sum(weights)+1)

for i in range(N):
    tmp=dp[:]
    dp[weights[i]]=True
    for j in range(len(dp)):
        if tmp[j]==True:
            if abs(j-weights[i])<len(dp):
                dp[abs(j-weights[i])]=True
            if j+weights[i]<len(dp):
                dp[j+weights[i]]=True

M=int(input())
checks=list(map(int, input().split()))

for i in checks:
    if i<len(dp) and dp[i]:
        print("Y", end=" ")
    else:
        print("N", end=" ")