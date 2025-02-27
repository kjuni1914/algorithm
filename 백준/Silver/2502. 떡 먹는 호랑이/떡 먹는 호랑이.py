import sys

input=sys.stdin.readline

D, K=map(int, input().split())
dp=[0]*(D)
fibo=[0]*(D)
fibo[0]=1
for i in range(1, D):
    fibo[i]=fibo[i-1]+fibo[i-2]
if D==3:
    print(1)
    print(K-1)
    sys.exit()
for i in range(1, K-1):
    if i%fibo[D-3]==0:
        if (K-i)%fibo[D-2]==0:
            print(i//fibo[D-3])
            print((K-i)//fibo[D-2])
            sys.exit()