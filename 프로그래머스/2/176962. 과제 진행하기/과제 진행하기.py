def solution(plans):
    plans.sort(key= lambda x:x[1])
    plans.append(["", "24:00", "0"])
    left = []
    answer = []
    for i in range(len(plans) - 1):
        req = int(plans[i][2])
        st = toMin(plans[i][1])
        et = toMin(plans[i+1][1])
        if et-st == req:
            answer.append(plans[i][0])
        elif et-st > req:
            answer.append(plans[i][0])
            answer.extend(doLeft(left, et, st+req)) #잔여작업 처리, return 완료한 잔여작업리스트
        elif et-st < req:
            left.append([plans[i][0], req+st-et])
    while left:
        answer.append(left.pop()[0])
    return answer

def doLeft(left, nextTime, st):
    lt = nextTime-st
    res = []
    while left and lt > 0:
        tmp = left.pop()
        if tmp[1] > lt: # 덜끝난경우
            tmp[1] -= lt
            left.append(tmp)
            lt = 0
        else:
            lt -= tmp[1]
            res.append(tmp[0])
    return res

def toMin(t):
    h, m = int(t.split(":")[0]), int(t.split(":")[1])
    return h*60 + m

def etCalc(plan):
    return toMin(plan[1]) + int(plan[2])

def toClock(t):
    h, m = str(t//60), str(t%60)
    return h + ":" + m