import sys
input=sys.stdin.readline

N=int(input())

dp=[0]*(max(N, 4)+1)
dp[2]=3
if N>3:
    for i in range(3, N+1):
        if i%2!=0:
            dp[i]=0
        else:
            tmp=2
            k=0
            while k<=i:
                if k==2:
                    tmp+=3*dp[i-k]
                else:
                    tmp+=2*dp[i-k]
                k+=2
            dp[i]=tmp

print(dp[N])