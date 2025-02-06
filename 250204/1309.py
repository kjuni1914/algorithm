import sys

input=sys.stdin.readline
N=int(input())

dp=[3, 7, 17]
if N<=2:
    print(dp[N-1])
    sys.exit()
tmp=2
for i in range(3, N):
    tmp+=2*(i-1)-1
    res=dp[1]*3+4*tmp
    tmp=dp.pop(0)
    dp.append(res)
print(dp[2]%9901)