import sys
input=sys.stdin.readline

N=int(input())

dp=[0]*(max(N, 2)+1)
dp[2]=3
if N>3:
    for i in range(3, N+1):
        if i%2!=0:
            dp[i]=0
        else:
            k=i-2
            tmp=0
            while k>=i-k:
                tmp+=dp[k]*dp[i-k]
                k-=2
            dp[i]=tmp+6
    print(dp)
print(dp[N])