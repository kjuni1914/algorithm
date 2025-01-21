import sys

input=sys.stdin.readline

N=int(input())

dp=[1 if i**(1/2)==int(i**(1/2)) else 0 for i in range(N+1)]
for i in range(1, N+1):
    if dp[i]==0:
        j=0
        while j**2<=i/2:
            j+=1
            if dp[i]==0 or dp[i]>dp[i-j**2]+dp[j**2]:
                dp[i]=dp[i-j**2]+dp[j**2]

print(dp[N])