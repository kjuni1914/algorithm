import sys

input=sys.stdin.readline

N=int(input())
if N==1:
    print(0)
    sys.exit()
dp=[0, 1]
for i in range(1, N):
    dp=[dp[1]%10, sum(dp)%10]

print(sum(dp)%10)