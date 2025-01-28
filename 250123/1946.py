import sys

input=sys.stdin.readline

for _ in range(int(input())):
    candidate=[]
    for i in range(int(input())):
        score0, score1=map(int, input().split())
        candidate.append((score0, score1))
    candidate.sort()
    ans=1
    cmp=candidate[0][1]
    for i in range(1, len(candidate)):
        if cmp>candidate[i][1]:
            ans+=1
            cmp=candidate[i][1]
    print(ans)