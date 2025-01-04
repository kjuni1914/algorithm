# https://school.programmers.co.kr/learn/courses/30/lessons/250125

def solution(board, h, w):
    for i in board:
        i.append(0)
        i.insert(0, 0)
    temp = [[0 for i in range(len(board[0]))]]
    temp.extend(board)
    temp2 = [0 for i in range(len(board[0]))]
    temp.append(temp2)
    X = temp[h+1][w+1]
    res = 0
    if temp[h][w+1] == temp[h+1][w+1]:
        res+=1
    if temp[h+1][w] == temp[h+1][w+1]:
        res+=1
    if temp[h+2][w+1] == temp[h+1][w+1]:
        res+=1
    if temp[h+1][w+2] == temp[h+1][w+1]:
        res+=1
    return res