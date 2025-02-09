def solution(players, callings):
    i = 1
    num = len(players)
    name = {}
    rank = {}
    for k in players:
        name[k] = i
        rank[i] = k
        i+=1
        
    for i in callings:
        tmpRank = name[i]
        loss = rank[tmpRank-1]
        name[i] -= 1
        name[loss] += 1
        rank[tmpRank] = loss
        rank[tmpRank-1] = i

    answer = []
    
    for i in rank:
        answer.append(rank[i])
    return answer