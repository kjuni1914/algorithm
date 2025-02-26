import sys

input=sys.stdin.readline

N=int(input())

houses=[]
for i in range(N):
    houses.append(list(map(int, input().split())))

tmpres=[]
for k in range(3):
    for i in range(N):
        if i==0:
            dp=[float('inf') if k!=idx else houses[0][idx] for idx in range(3)]
        else:
            tmp=dp[:]
            cost=houses[i]
            for j in range(3):
                dp[j]=min(tmp[(j-1)], tmp[j-2])+cost[j]
    tmpres.append(min(dp[k-1], dp[k-2]))

print(min(tmpres))