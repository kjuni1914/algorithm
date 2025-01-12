# https://school.programmers.co.kr/learn/courses/30/lessons/250137

def solution(bandage, health, attacks):
    maxHealth = health
    cont = 0
    turn = attacks[len(attacks)-1][0]
    for i in range(turn+1):
        if i==attacks[0][0]:
            cont = 0
            health -= attacks.pop(0)[1]
            if health <= 0:
                return -1
        else:
            if cont == bandage[0]-1:
                health += bandage[1]+bandage[2]
                cont = 0
            else:
                health += bandage[1]
                cont+=1
                
        health = min(maxHealth, health)

        
    return health