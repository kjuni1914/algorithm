import sys
input=sys.stdin.readline
dp=[[1, 0, 0], [0, 1, 0], [1, 1, 1]]
prev=3

for _ in range(int(input())):
    N=int(input())
    if N<4:
        print(sum(dp[N-1]))
        continue
    for i in range(prev, N):
        dp.append([(dp[i-1][1]+dp[i-1][2])%1000000009, (dp[i-2][0]+dp[i-2][2])%1000000009, (dp[i-3][0]+dp[i-3][1])%1000000009])
    if prev<N:
        prev=N
    print(sum(dp[N-1])%1000000009)