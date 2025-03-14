import sys

input=sys.stdin.readline

N=int(input())

dp=[0]*(N+1)

for i in range(1, N+1):
    candidate=[]
    if i==1 or i**(1/2)==int(i**(1/2)):
        dp[i]=1
        continue
    j=1
    while j**2<=i:
        candidate.append(dp[i-j**2]+dp[j**2])
        j+=1
    dp[i]=min(candidate)
    
print(dp[N])