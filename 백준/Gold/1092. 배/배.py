import sys

input=sys.stdin.readline

N=int(input())
crain=list(map(int, input().split()))
M=int(input())
box=list(map(int, input().split()))

crain.sort()
box.sort()

weight=[[] for _ in range(N)]
idx=0
for i in box:
    while crain[idx]<i:
        idx+=1
        if idx==N:
            print(-1)
            sys.exit()

    weight[idx].append(i)

ans=0
cnt=0

while cnt<M:
    ans+=1
    for i in range(N-1, -1, -1):
        while i>0 and not weight[i]:
            i-=1
        if weight[i]:
            weight[i].pop()
            cnt+=1

print(ans)