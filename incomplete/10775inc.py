import sys

input=sys.stdin.readline

G=int(input())
P=int(input())

ans=0

parent=[i for i in range(G+1)]

def find(x):
    if parent[x]==x:
        return x
    parent[x]=find(parent[x])
    return find(parent[x])

def union(a, b):
    a=find(a)
    b=find(b)
    if a>b:
        a, b=b, a
    parent[b]=a

open=True
for i in range(P):
    plane=int(input())
    if open and find(plane)!=0:
        ans+=1
        union(find(plane), find(plane)-1)
    else:
        open=False

print(ans)