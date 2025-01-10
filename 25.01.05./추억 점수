# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    answer = []
    dic = dict()
    for i, j in zip(name, yearning):
        dic[i]=j
    for i in photo:
        tmp = 0
        for j in i:
            if j in dic:
                tmp+=dic[j]
        answer.append(tmp)
    return answer