import sys

input=sys.stdin.readline
N=int(input())

dp=[float('inf')]*max(2, (N+1))
dp[1]=0
path=[0]*max(2, (N+1))

for i in range(2, N+1):
    dp[i]=dp[i-1]+1
    path[i]=i-1
    
    if i%2==0 and dp[i//2]+1<dp[i]:
        dp[i]=dp[i//2]+1
        path[i]=i//2
    
    if i%3==0 and dp[i//3]+1<dp[i]:
        dp[i]=dp[i//3]+1
        path[i]=i//3

print(dp[N])

while N>1:
    print(N, end=" ")
    N=path[N]
print(1, end="\n")