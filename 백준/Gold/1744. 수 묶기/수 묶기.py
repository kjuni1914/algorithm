import sys
import heapq

input=sys.stdin.readline
N=int(input())

pos=[]
neg=[]
res=0

for i in range(N):
    num=int(input())
    if num==1:
        res+=1
    elif num>0:
        heapq.heappush(pos, -num)
    else:
        heapq.heappush(neg, num)

while pos:
    num1=heapq.heappop(pos)
    if pos:
        num2=heapq.heappop(pos)
        res+=num1*num2
    else:
        res-=num1

while neg:
    num1=heapq.heappop(neg)
    if neg:
        num2=heapq.heappop(neg)
        res+=num1*num2
    else:
        res+=num1

print(res)