import sys
import heapq

input=sys.stdin.readline
N=int(input())

pos=[]
neg=[]
zero=[]
for i in range(N):
    num=int(input())
    if num>0:
        heapq.heappush(pos, -num)
    elif num<0:
        heapq.heappush(neg, num)
    else:
        zero.append(num)

res=0
flag=False
prev=0

while pos and pos[0]<-1:
    if not flag:
        prev=heapq.heappop(pos)
        flag=True
    else:
        res+=prev*heapq.heappop(pos)
        prev=0
        flag=False

if flag:
    res-=prev
    prev=0
res-=sum(pos)
flag=False

while neg:
    if not flag:
        prev=heapq.heappop(neg)
        flag=True
    else:
        res+=prev*heapq.heappop(neg)
        prev=0
        flag=False
        
if zero:
    print(res)
else:
    res+=prev
    print(res)