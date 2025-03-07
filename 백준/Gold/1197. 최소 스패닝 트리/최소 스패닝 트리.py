import sys

input=sys.stdin.readline

V, E=map(int, input().split())
parent=[i for i in range(V)]
rank=[1]*V

def find(a):
    if a==parent[a]:
        return a
    parent[a]=find(parent[a])
    return parent[a]

def union(a, b):
    a, b=find(a), find(b)
    if a==b:
        return False
    
    if rank[a]<rank[b]:
        a, b=b, a
    parent[b]=a
    if rank[a]==rank[b]:
        rank[a]+=1
    return True

edges=[]
for _ in range(E):
    st, end, cost=map(int, input().split())
    edges.append((cost, (st-1, end-1)))
edges.sort(reverse=True)

ans=0
for i in range(E):
    cost, edge=edges.pop()
    if union(edge[0], edge[1]):
        ans+=cost

print(ans)