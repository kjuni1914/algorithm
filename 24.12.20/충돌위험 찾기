# https://school.programmers.co.kr/learn/courses/30/lessons/340211#

import random

def solution(points, routes):
    answer = 0
    line = [[] for i in range(len(routes))]
    for i in range(len(routes)):
        for j in range(len(routes[i]) - 1):
            st = points[routes[i][0+j] - 1]
            if j == 0:
                line[i].append(tuple(st))
            end = points[routes[i][1+j] - 1]
            arc(st, end, line[i])
    line = lenSame(line)
    
    for i in range(len(line[0])):
        temp = []
        for j in range(len(line)):
            temp.append(line[j][i])
        for k in set(temp):
            if temp.count(k) != 1:
                answer+=1
    return answer

def arc(st, end, line):
    st = st.copy()
    end = end.copy()
    temp = []

    while 1:
        if st[0] == end[0] and st[1] == end[1]:
            line.extend(temp)
            break
        else:
            if st[0] != end[0]:
                if st[0] < end[0]:
                    st[0] += 1
                if st[0] > end[0]:
                    st[0] -= 1
            else:
                if st[1] < end[1]:
                    st[1] += 1
                if st[1] > end[1]:
                    st[1] -= 1
            temp.append(tuple(st))
        
def lenSame(A):
    maxLen = max(len(arr) for arr in A)
    newA = [arr + [(random.random(), random.random())]*(maxLen-len(arr)) for arr in A]
    return newA
