import sys

input=sys.stdin.readline

N=int(input())

dp=[[0]* N for _ in range(N)]
dp[0][0]=1

field=[]
for _ in range(N):
    field.append(list(map(int, input().split())))

def sol():
    for i in range(N):
        for j in range(N):
            if i==N-1 and j==N-1:
                return
            power=field[i][j]
            if i+power<N:
                dp[i+power][j]+=dp[i][j]
            if j+power<N:
                dp[i][j+power]+=dp[i][j]

sol()
print(dp[N-1][N-1])