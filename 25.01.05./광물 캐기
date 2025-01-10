# https://school.programmers.co.kr/learn/courses/30/lessons/172927

def solution(picks, minerals):
    power = []
    tmp = [0, 0, 0]
    j = 0
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            tmp[0]+=1
            tmp[1]+=5
            tmp[2]+=25
        elif minerals[i] == "iron":
            tmp[0]+=1
            tmp[1]+=1
            tmp[2]+=5
        else:
            tmp[0]+=1
            tmp[1]+=1
            tmp[2]+=1
            
        if (i%5 == 4 or i == len(minerals) - 1) and j < sum(picks):
            power.append(tmp)
            tmp = [0, 0, 0]
            j+=1
    use = [0, 0, 0]
    tmp = 0
    while tmp != len(power):
        if picks[0] > 0:
            picks[0]-=1
            use[0]+=1
            tmp+=1
        elif picks[1] > 0:
            picks[1]-=1
            use[1]+=1
            tmp+=1
        elif picks[2]>0:
            picks[2]-=1
            use[2]+=1
            tmp+=1
    power.sort(key = lambda x:(-x[2], -x[1]))

    answer = 0
    
    while power:
        tmp = power.pop()
        if use[2]>0:
            use[2]-=1
            answer+=tmp[2]
        elif use[1] > 0:
            use[1]-=1
            answer+=tmp[1]
        elif use[0] > 0:
            use[0]-=1
            answer+=tmp[0]

    return answer