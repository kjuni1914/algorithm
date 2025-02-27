import sys

input=sys.stdin.readline
N=int(input())

costs=[]
for i in range(N):
    costs.append(list(map(int, input().split())))

res=[]
for i in range(3):
    for j in range(N):
        if j==0:
            dp=[costs[j][idx] if idx==i else float('inf') for idx in range(3)]
        else:
            tmp=dp[:]
            for k in range(3):
                tmp[k]=min(dp[k-1], dp[k-2])+costs[j][k]
            dp=tmp
        
    res.append(min(dp[i-1], dp[i-2]))

print(min(res))