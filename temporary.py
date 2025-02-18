import sys
input=sys.stdin.readline

N, M=map(int, input().split())

nums=list(map(int, input().split()))

nums.sort()

def backt(idx, path, visited=[False]*len(nums)):
    if len(path)==M:
        print(" ".join(path))
    prev=float('inf')
    for i in range(len(nums)):
        if not visited[i] and prev!=nums[i]:
            visited[i]=True
            path.append(str(nums[i]))
            backt(i, path, visited)
            visited[i]=False
            path.pop()
            prev=nums[i]
    return 

backt(N+1, [])