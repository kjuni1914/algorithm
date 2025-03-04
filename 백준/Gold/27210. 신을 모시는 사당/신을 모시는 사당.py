import sys
sys.setrecursionlimit(10**8)

input=sys.stdin.readline

N=int(input())
stone=list(map(int, input().split()))

dp1=[0]*N
dp2=[0]*N

res=0
for i in range(N):
    if stone[i]==1:
        dp1[i]=max(dp1[i-1]+1, dp1[i])
        dp2[i]=max(dp2[i-1]-1, dp2[i])
    else:
        dp1[i]=max(dp1[i-1]-1, dp1[i])
        dp2[i]=max(dp2[i-1]+1, dp2[i])
    res=max(dp1[i], dp2[i], res)

print(res)