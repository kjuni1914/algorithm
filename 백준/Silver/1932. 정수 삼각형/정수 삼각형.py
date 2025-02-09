import sys
input=sys.stdin.readline

N=int(input())

for i in range(N):
    row=list(map(int, input().split()))
    if i==0:
        dp=[row[0]]
        continue
    else:
        tmp=[]
        for j in range(len(row)):
            if j==0:
                tmp.append(dp[0]+row[0])
            elif j==len(row)-1:
                tmp.append(dp[j-1]+row[j])
            else:
                tmp.append(max(dp[j-1:j+1])+row[j])
        dp=tmp

print(max(dp))