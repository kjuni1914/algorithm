import sys

input=sys.stdin.readline

N=int(input())
friends={i:set() for i in range(N)}
res={i:set()|friends[i] for i in range(N)}

for i in range(N):
    tmp=input()
    for j in range(N):
        if tmp[j]=="Y":
            friends[i].add(j)

for i in friends:
    search=list(friends[i])
    level=0
    while level<=1:
        while search:
            tmp=search.pop()
            res[i].add(tmp)
            for j in friends[tmp]:
                if j not in res[i]:
                    res[i].add(j)
        level+=1
ans=max([len(res[i]) for i in res.keys()])-1
if ans!=-1:
    print(ans)
else:
    print(0)