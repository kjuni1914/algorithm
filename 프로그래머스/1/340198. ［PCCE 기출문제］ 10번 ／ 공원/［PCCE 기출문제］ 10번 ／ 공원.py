def solution(mats, park):
    temp = 0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "-1":
                temp = max(temp, square(park, i, j))
    answer = [mats[i] if mats[i] <= temp else -1 for i in range(len(mats))]
    return max(answer)

def square(mat, i, j):
    res = 1
    while 1:
        for k in range(res):
            for l in range(res):
                if i+k >= len(mat) or j+l >= len(mat[0]):
                    return res-1
                if mat[i+k][j+l] != "-1":
                    return res-1
        res+=1
                