import sys
import heapq

input=sys.stdin.readline

N=int(input())
num=list(map(int, input().split(" ")))
center={i+1:[(i+1, i+1)] for i in range(N)}
M=int(input())

for _ in range(M):
    S, E=map(int, input().split(" "))
    if S==E:
        print(1)
    else:
        tmpS=S
        tmpE=E
        while tmpS<center[int((S+E)/2)][0][0] and tmpS<tmpE:
            if num[tmpS-1]!=num[tmpE-1]:
                print(0)
                break
            tmpS+=1
            tmpE-=1
        else:
            if num[tmpS-1]!=num[tmpE-1]:
                print(0)
            else:
                heapq.heappush(center[int((S+E)/2)], (S, E))
                print(1)