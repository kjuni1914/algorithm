import sys

input=sys.stdin.readline

N=int(input())
friends={i:set() for i in range(N)}

for i in range(N):
    tmp=input()
    for j in range(N):
        if tmp[j]=="Y":
            friends[i].add(j)

def dfs(N, level, depth, visited):
    if depth==level:
        return
    for i in friends[N]:
        if i not in visited:
            visited.add(i)
            dfs(i, level, depth+1, visited)

ans=[]

for i in friends:
    visited=set()
    ans.append(len(dfs(i, 2, 0, visited))-1)

print(max(ans) if max(ans)!=-1 else 0)