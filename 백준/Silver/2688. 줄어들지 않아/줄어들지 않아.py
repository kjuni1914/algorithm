import sys

input=sys.stdin.readline

dp=[1]*10
prev=0
ans=[10]
query=[]

for _ in range(int(input())):
    N=int(input())-1
    query.append(N)
    for i in range(prev, N):
        for j in range(10):
            dp[j]=sum(dp[j:])
        ans.append(sum(dp))
    print(ans[N])
    prev=N