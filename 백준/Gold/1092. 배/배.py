import sys

input=sys.stdin.readline

N=int(input())
crain=list(map(int, input().split()))
M=int(input())
box=list(map(int, input().split()))

crain.sort(reverse=True)
box.sort(reverse=True)

if box[0]>crain[0]:
    print(-1)
    sys.exit()

cnt=0
while box:
    cnt+=1
    i=0
    for c in crain:
        if not box or c<box[-1]:
            break
        while i<M and c<box[i]:
            i+=1
        box.pop(i)

print(cnt)