def solution(sequence, k):
    s = 0
    e = len(sequence)-1
    summation = 0
    for i in range(len(sequence)-1, -1, -1):
        summation += sequence[i]
        if summation > k:
            summation-=sequence.pop()
            e-=1
        if summation == k:
            while sequence[i-1] == sequence[-1] and i>=1:
                i-=1
                e-=1
            answer = [i, e]
            return answer
    return answer