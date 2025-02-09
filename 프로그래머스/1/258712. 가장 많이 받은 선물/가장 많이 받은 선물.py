def solution(friends, gifts):
    dic=dict()
    for i in friends:
        dic[i]=[dict(), 0]
        for j in friends:
            dic[i][0][j] = 0

    for j in gifts:
        give=j.split(" ")[0]
        take=j.split(" ")[1]
        if take not in dic[give][0]:
            dic[give][0][take]=1
        else:
            dic[give][0][take]+=1 
        
        dic[give][1]+=1
        dic[take][1]-=1
    answer = dict()
    for i in friends:
        answer[i] = 0
    for i in friends:
        for j in dic[i][0]:
            if dic[i][0].get(j)<dic[j][0].get(i):
                answer[j]+=1
            elif dic[i][0].get(j)>dic[j][0].get(i):
                answer[i]+=1
            else:
                if dic[i][1]>dic[j][1]:
                    answer[i]+=1
                elif dic[i][1]<dic[j][1]:
                    answer[j]+=1
    return int(max(answer.values())/2)