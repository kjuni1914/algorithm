# https://school.programmers.co.kr/learn/courses/30/lessons/258711

def solution(edges):
    answer = [0] * 4
    who = dict()
    
    for i in edges:
        if i[0] not in who:
            who[i[0]]=[0, 0]
        if i[1] not in who:
            who[i[1]]=[0, 0]
            
    for i in edges:
        who[i[0]][0] += 1
        who[i[1]][1] += 1
        
    answer[0] = max(who.keys(), key=lambda x: who[x][0] - who[x][1])
    temp = who[answer[0]]
    
    for i in edges:
        if i[0] == answer[0]:
            who[i[1]][1] -= 1
    for i in who:
        if i == answer[0]:
            continue
        if who[i][0] == 2 and who[i][1] == 2:
            answer[3] += 1
        elif who[i][0] == 0 and who[i][1] == 1 or (who[i][0] == 0 and who[i][1] == 0):
            answer[2] += 1

    answer[1] = temp[0] - answer[2] - answer[3]

    return answer