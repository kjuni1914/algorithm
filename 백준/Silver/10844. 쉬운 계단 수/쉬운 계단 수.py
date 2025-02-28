import sys
input=sys.stdin.readline

N=int(input())
dp=[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(N-1):
    tmp=[0]*10
    tmp[0]=dp[1]%1000000000
    for j in range(1, 9):
        tmp[j]=(dp[j-1]+dp[j+1])%1000000000
    tmp[9]=dp[8]%1000000000
    dp=tmp
print(sum(dp)%1000000000)