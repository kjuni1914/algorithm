import sys

input=sys.stdin.readline

N=int(input())
field=[]


dp=[0, 0, 0]

for i in range(N):
    costs=list(map(int, input().split()))
    tmp=dp.copy()
    for j in range(3):
        dp[j]=min(tmp[(j+1)%3], tmp[(j+2)%3])+costs[j]
print(min(dp))