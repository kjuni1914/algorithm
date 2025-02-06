import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N=int(input())
    scores=[]
    for i in range(2):
        scores.append(list(map(int, input().split())))
    dp=[[0 for _ in range(N)] for _ in range(2)]
    for j in range(N):
        for i in range(2):
            if j==0:
                dp[i][j]=scores[i][j]
            elif j==1:
                dp[i][j]=scores[i][j]+scores[i-1][j-1]
            else:
                dp[i][j]=scores[i][j]+max(dp[i][j-2]+scores[i-1][j-1], dp[i-1][j-2])
        print(dp)
    print(max(dp[0][N-1], dp[1][N-1]))
