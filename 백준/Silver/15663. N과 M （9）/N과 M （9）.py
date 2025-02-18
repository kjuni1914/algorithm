import sys
input=sys.stdin.readline

N, M=map(int, input().split())

nums=list(map(int, input().split()))

nums.sort()

def backt(idx, path, visited=[False]*len(nums), res=None):
    if res==None:
        res=set()
    if len(path)==M:
        tmp=" ".join(path)
        if tmp not in res:
            res.add(tmp)
            print(tmp)
    
    for i in range(len(nums)):
        if not visited[i]:
            visited[i]=True
            path.append(str(nums[i]))
            backt(i, path, visited, res)
            visited[i]=False
            path.pop()
    
    return res

backt(N+1, [])