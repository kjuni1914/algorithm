import sys

input=sys.stdin.readline
N=int(input())

dp=[None]*max(4, (N+1))
length=[float('inf')]*max(4, (N+1))

dp[1], dp[2], dp[3]=[1], [2, 1], [3, 1]
length[1], length[2], length[3]=0, 1, 1

for i in range(4, N+1):
    if i%6==0:
        if length[i//3]>length[i//2]:
            length[i]=length[i//2]+1
            dp[i]=[i]+dp[i//2]
        else:
            length[i]=length[i//3]+1
            dp[i]=[i]+dp[i//3]
    elif i%3==0:
        length[i]=length[i//3]+1
        dp[i]=[i]+dp[i//3]
    elif i%2==0:
        length[i]=length[i//2]+1
        dp[i]=[i]+dp[i//2]
    else:
        length[i]=length[i-1]+1
        dp[i]=[i]+dp[i-1]

    if length[i-1]+1<length[i]:
        length[i]=length[i-1]+1
        dp[i]=[i]+dp[i-1]

print(length[N])
print(" ".join([str(i) for i in dp[N]]))