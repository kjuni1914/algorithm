import sys
import copy
from collections import deque

def bfs(stNode, endPnt):
    search = deque([stNode])
    visted = [0] * 200001
    res = 0
    cnt = 0
    while search: 
        flag = False
        for _ in range(len(search)):
            tmp = search.popleft()
            if tmp == endPnt:
                cnt += 1
                flag = True
            for i in tmp-1, tmp+1, tmp*2:
                if (visted[i]==0 or visted[i] == visted[tmp]+1) and 0<=i<=100000:
                    visted[i]=visted[tmp]+1
                    search.append(i)
        if flag == True:
            print(f"{res}\n{cnt}")
            return
        res +=1

input = sys.stdin.readline

cmd1, cmd2 = map(int, input().split(" "))

t = bfs(cmd1, cmd2)