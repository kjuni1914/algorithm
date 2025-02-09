def solution(targets):
    answer = 0
    bound = 0
    targets.sort(key=lambda x: x[0])
    for s, e in targets:
        if s < bound:
            bound = min(e, bound)
        else:
            bound = e
            answer+=1
    return answer