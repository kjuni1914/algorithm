import sys
input=sys.stdin.readline

# 절반 고르면 나머지 절반은 자동으로 게산
# 백트래킹 하면서 res 에 둘 차의 절댓값 넣고 최소 출력

N=int(input())

matrix=[]

for _ in range(N):
    matrix.append(list(map(int, input().split())))

def comb(st, path, res=None):
    if res==None:
        res=[]
    if len(path)==N//2:
        res.append(path[:]) 
        return
    
    for i in range(st, N):
        path.append(i)
        comb(i+1, path, res)
        path.pop()
    return res

def permu2(nums, st, path, res=None):
    if res==None:
        res=[]

    if len(path)==2:
        res.append(path[:]) 
        return
    
    for i in range(st, len(nums)):
        path.append(nums[i])
        permu2(nums, i+1, path, res)
        path.pop()

    return res

homes=comb(0, [])
all=set([i for i in range(N)])
candidate=[]

for home in homes[:len(homes)//2]:
    away=list(all-set(home))
    hsynergy=0
    for i in permu2(home, 0, []):
        x, y=i
        hsynergy+=matrix[x][y]+matrix[y][x]
    asynergy=0
    for i in permu2(away, 0, []):
        x, y=i
        asynergy+=matrix[x][y]+matrix[y][x]

    candidate.append(abs(hsynergy-asynergy))

print(min(candidate))