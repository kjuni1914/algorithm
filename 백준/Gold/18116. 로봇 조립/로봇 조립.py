import sys

input=sys.stdin.readline

parent=[i for i in range(1000001)]
rank=[1]*1000001

def find(a):
    if a==parent[a]:
        return a
    parent[a]=find(parent[a])
    return parent[a]

def union(a, b):
    a=find(a)
    b=find(b)
    if a!=b:
        if rank[a]>rank[b]:
            a, b=b, a
        parent[a]=b
        rank[b]=rank[a]+rank[b]

for _ in range(int(input())):
    cmd=input().split()
    if cmd[0]=="I":
        union(int(cmd[1]), int(cmd[2]))
    elif cmd[0]=="Q":
        print(rank[find(int(cmd[1]))])