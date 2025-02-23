import sys

input=sys.stdin.readline
N=int(input())
dp=[0, 0, 0]
for i in range(N):
    now=int(input())
    tmp=dp[:]
    if i==0:
        tmp[1]+=now
        tmp[2]+=now
    else:
        tmp[0]=max(dp)
        tmp[1]=dp[0]+now
        tmp[2]=dp[1]+now
    dp=tmp

print(max(dp))