import sys

input=sys.stdin.readline

N=int(input())
stair=[]
for _ in range(N):
    stair.append(int(input()))
if N<=2:
    print(sum(stair))
    sys.exit()
dp=[stair[0]+stair[1], stair[0], stair[1]]
for i in range(2, N):
    dp=[dp[2]+stair[i], max(dp[0], dp[2]), dp[1]+stair[i]]

print(max(dp[0], dp[2]))