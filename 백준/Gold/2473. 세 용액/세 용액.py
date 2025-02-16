import sys
input=sys.stdin.readline

N=int(input())

nums=list(map(int, input().split()))

nums.sort()

tmpres=float("inf")

for i in range(N-2):
    st=i+1
    end=N-1
    while st<end:
        tmpsum=nums[i]+nums[st]+nums[end]
        if abs(tmpsum)<tmpres:
            ans=[nums[i], nums[st], nums[end]]
            tmpres=abs(tmpsum)
        if tmpsum<0:
            st+=1
        elif tmpsum>0:
            end-=1
        else:
            print(" ".join([str(i) for i in ans]))
            sys.exit()

print(" ".join([str(i) for i in ans]))