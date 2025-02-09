import sys
input = sys.stdin.readline

cmd = input().split()
a = int(cmd[0])
b = int(cmd[1])
l = []

dp = [[0 for _ in range(b+1)] for _ in range(a)]

for _ in range(a):
    i = input().split()
    l.append([int(i[0]), int(i[1])])

res = 0
for i in range(a):
    for j in range(b + 1):
        if i == 0:
            if j >= l[i][0]:
                dp[i][j] = l[i][1]
        else:
            if j >= l[i][0]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-l[i][0]] + l[i][1])
            else:
                dp[i][j] = dp[i-1][j]
        res = max(res, dp[i][j])

print(res)
