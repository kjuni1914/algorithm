import sys

input=sys.stdin.readline

N, K=map(int, input().split())

prev=-1
if bin(N).count("1")<=K:
    print(0)
    sys.exit()

ans=0
now=N
for i in range(len(bin(N))):
    buy=now&-now
    now+=buy
    ans+=buy
    if bin(now).count("1")<=K:
        print(ans)
        break
    