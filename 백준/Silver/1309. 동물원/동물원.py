import sys

input=sys.stdin.readline
N=int(input())

for i in range(N):
    if i==0:
        dp=[1, 2]
    else:
        dp=[sum(dp), 2*dp[0]+dp[1]]
    
print(sum(dp)%9901)