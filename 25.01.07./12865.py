import sys
input = sys.stdin.readline

n, k=map(int, input().split())

dp=[[0 for j in range(k+1)] for i in range(n)]
l1=[]

for _ in range(n):
    l1.append(tuple(map(int, input().split())))

for i in range(n):
    for j in range(k+1):
        if i == 0:
            if j >= l1[i][0]:
                dp[i][j] = l1[i][1]
        else:
            if j < l1[i][0]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - l1[i][0]] + l1[i][1])

print(dp[-1][k])