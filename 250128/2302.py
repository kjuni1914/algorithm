import sys

input=sys.stdin.readline

N=int(input())
M=int(input())
MVP=[]
dp=[0]*(41)
for i in range(M):
    MVP.append(int(input()))
dp[0]=1
dp[1]=1
dp[2]=2
dp[3]=3
for i in range(4, N+1):
    dp[i]=dp[i-2]+dp[i-1]
ans=1
tmp=0

for i in MVP:
    ans*=dp[i-tmp-1]
    tmp=i
    
ans*=dp[N-tmp]

print(ans)