import sys

input=sys.stdin.readline

N, k=map(int, input().split())
num=str(input()).strip()
num=[num[i] for i in range(len(num))]

res=[]
# 순회하면서
# k-=1 시키면서 최댓값 저장
# 최댓값 갱신할 때 tmp=k 저장
# k=0일 때 최댓값을 res에 넣고, k=tmp 하고 쭉 진행
maxi=0
tmpk=k
cnt=1
for i in range(N):
    if k==0:     
        res.append(str(maxi)*cnt)
        maxi=int(num[i])
        cnt=1
        if tmpk==0:
            break
        k=tmpk
    else:
        if maxi<=int(num[i]):
            if maxi==int(num[i]):
                cnt+=1
            else:
                maxi=int(num[i])
                cnt=1
                tmpk=k
        k-=1
res.extend(num[i:len(num)])
print("".join(res))