import copy
import sys

input=sys.stdin.readline

weight=int(input())

sugar=[5, 3]
dp=[[[0, 0] for _ in range(weight+1)] for _2 in range(len(sugar))]

for i in range(len(sugar)):
    for j in range(1, weight+1):
        if i==0:
            dp[i][j][0]=j//sugar[i]
            dp[i][j][1]=sugar[i]*dp[i][j][0]
        else:
            if j>=sugar[i]:
                if dp[i-1][j][1]<dp[i][j-sugar[i]][1]+sugar[i]:
                    dp[i][j][1]=dp[i][j-sugar[i]][1]+sugar[i]
                    dp[i][j][0]=dp[i][j-sugar[i]][0]+1
                else:
                    dp[i][j][0]=dp[i-1][j][0]
                    dp[i][j][1]=dp[i-1][j][1]
            else:
                dp[i][j]=copy.deepcopy(dp[i-1][j])

if dp[len(sugar)-2][weight][1]==weight or dp[len(sugar)-1][weight][1]==weight:
    if dp[len(sugar)-1][weight][1]==weight:
        print(dp[len(sugar)-1][weight][0])
    else: print(dp[len(sugar)-2][weight][0])
else:
    print(-1)