import sys

input=sys.stdin.readline

cmd = int(input())

minScore=[0 for _1 in range(3)]
maxScore=[0 for _1 in range(3)]

for i in range(cmd):
    tmp=list(map(int, input().split(" ")))
    mintmp=minScore.copy()
    maxtmp=maxScore.copy()
    for j in range(3):
        if j==0:
            minScore[j]=min(mintmp[0:2])+tmp[j]
            maxScore[j]=max(maxtmp[0:2])+tmp[j]
        elif j==1:
            minScore[j]=min(mintmp[0:3])+tmp[j]
            maxScore[j]=max(maxtmp[0:3])+tmp[j]
        else:
            minScore[j]=min(mintmp[1:3])+tmp[j]
            maxScore[j]=max(maxtmp[1:3])+tmp[j]

print(max(maxScore), min(minScore))