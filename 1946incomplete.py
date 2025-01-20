import sys
import heapq

input=sys.stdin.readline

for _ in range(int(input())):
    num=int(input())
    candidate=[]
    for _ in range(num):
        tmp=list(map(int, input().split(" ")))
        if not candidate:
            candidate.append([tmp[0], tmp[1]])
        else:
            threshold=len(candidate)
            new_cand=[]
            for i in candidate:
                flag=False
                if i[0]>tmp[0] and i[1]>tmp[1]:
                    continue
                else:
                    new_cand.append(i)
                    if i[0]<tmp[0] and i[1]<tmp[1]:
                        flag=True
                        break
            candidate=new_cand
            if not flag:
                candidate.append(tmp)

    print(len(candidate))