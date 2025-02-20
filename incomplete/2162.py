import sys

input=sys.stdin.readline

N=int(input())

parent=[i for i in range(N)]
rank=[1]*N

def find(a):
    if a==parent[a]:
        return a
    parent[a]=find(parent[a])
    return parent[a]

def union(a, b):
    a=find(a)
    b=find(b)

    if rank[a]<rank[b]:
        a, b=b, a
    parent[b]=a
    rank[a]+=rank[b]

lines=[]

for i in range(N):
    x1, y1, x2, y2=map(int, input().split())
    if x1>x2:
        x1, x2=x2, x1
        y1, y2=y2, y1
    elif x1==x2:
        if y1>y2:
            x1, x2=x2, x1
            y1, y2=y2, y1

    if i>0:
        if ((x1-prevx2)*(x2-prevx1)<=0 and (y1-prevy2)*(y2-prevy1)<=0) or (x1, y1)==(prevx1, prevy1) or (x2, y2)==(prevx2, prevy2):
            union(i, previdx)
    
    prevx1, prevy1, prevx2, prevy2, previdx=x1, y1, x2, y2, i

for i in range(N):
    find(i)

print(parent)
print(rank)