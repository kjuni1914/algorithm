import sys

input=sys.stdin.readline

N=int(input())

dp=[0]*(N+1)

for i in range(1, N+1):
    if i==1 or i**(1/2)==int(i**(1/2)):
        dp[i]=1
        continue
    j=1
    while j**2<=i:
        if dp[i]==0 or dp[i]>dp[i-j**2]+dp[j**2]:
            dp[i]=dp[i-j**2]+dp[j**2]
        j+=1
    
print(dp[N])