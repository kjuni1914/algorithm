import sys

input=sys.stdin.readline

N=int(input())

nums=list(map(int, input().split()))

operators=list(map(int, input().split()))

def backtracking(tmpres, st, res=[]):
    if st==N-1:
        res.append(tmpres)
        return
    
    tmp=tmpres
    for j in range(4):
        if operators[j]>0:
            operators[j]-=1
            if j==0:
                tmpres+=nums[st+1]
            elif j==1:
                tmpres-=nums[st+1]
            elif j==2:
                tmpres*=nums[st+1]
            else:
                if tmpres<0:
                    tmpres=-(-tmpres//nums[st+1])
                else:
                    tmpres//=nums[st+1]

            backtracking(tmpres, st+1)
            operators[j]+=1
            tmpres=tmp
        else:
            continue

    return res

print(max(backtracking(nums[0], 0)))
print(min(backtracking(nums[0], 0)))