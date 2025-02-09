import sys
input=sys.stdin.readline

amount=int(input())
materials=list(map(int, input().split(" ")))

materials.sort()
i, j=0, len(materials)-1
tmpi=materials[i]
tmpj=materials[j]
tmpresult=float('inf')

while 1:
    tmp=materials[i]+materials[j]
    if tmpresult**2>tmp**2:
        tmpi=materials[i]
        tmpj=materials[j]
        tmpresult=tmp
    if tmp<0:
        i+=1
    elif tmp>0:
        j-=1
    else:break
    if i==j: break

print(tmpi, tmpj)