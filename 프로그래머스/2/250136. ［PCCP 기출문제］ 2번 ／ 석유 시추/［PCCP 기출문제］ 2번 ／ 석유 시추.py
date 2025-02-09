from collections import deque

def solution(land):
    answer = 0
    lane = [set() for i in range(len(land[0]))]
    cnt = 0
    deq = deque()
    checker = set()
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    dic = dict()
    for j in range(len(land[0])):
        for i in range(len(land)):
            cnt+=1
            trace = []
            res = 0
            if (i, j) not in checker and land[i][j] == 1:
                res = 1
                checker.add((i, j))
                deq.append([i, j])
                trace.append([i, j])
            while deq:
                temp = deq.popleft()
                tempi, tempj = temp[0], temp[1]
                for m in move:
                    di = tempi + m[0]
                    dj = tempj + m[1]
                    if (di, dj) not in checker:
                        if 0<=di<=len(land)-1 and 0<=dj<=len(land[0])-1 and land[di][dj] != 0:
                            deq.append([di, dj])
                            checker.add((di, dj))
                            trace.append([di, dj])
                            res+=1
            for k in trace:
                land[k[0]][k[1]] = [cnt, res]
                lane[k[1]].add(cnt)
            dic[cnt] = res
    for i in lane:
        if answer < sum(dic[j] for j in list(i)):
            answer = sum(dic[j] for j in list(i))
            
    return answer