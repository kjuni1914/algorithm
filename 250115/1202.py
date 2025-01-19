import sys
import heapq

input=sys.stdin.readline

cmd1, cmd2 = map(int, input().split(" "))
qhtjr=[]
bag=[]

for _ in range(cmd1):
    tmp=list(map(int, input().split(" ")))
    heapq.heappush(qhtjr, (tmp[0], tmp[1]))

res=0

for _ in range(cmd2):
    heapq.heappush(bag, int(input()))

candidate=[]
print(bag)
print(qhtjr)

while qhtjr:
    w, v=heapq.heappop(qhtjr)
    if bag[00] < w:
        res+=-candidate[0]
        if len(bag)>=2:
           heapq.heappop(bag)
        else:
            break
        candidate=[]
        
    else:
        heapq.heappush(candidate, -v)

if bag:
    res+=-candidate[0]

print(res)