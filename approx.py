import random as r

n = 10      # 참여자 수
m = 1000    # 시행 횟수


def RPS(n):
    rps = []    # r 0 / p 1 / s 2
    for i in range(n):
        rps.append(r.randint(0,2))
        
    return rps

def win(rps):
    roc = 0
    pap = 0
    sci = 0

    winner = 0

    for i in rps:
        if i == 0:
            roc += 1
        elif i == 1:
            pap += 1
        elif i == 2:
            sci += 1

    if (roc != 0 and pap == 0 and sci != 0):
        winner = roc
    elif (roc != 0 and pap != 0 and sci == 0):
        winner = pap
    elif (roc == 0 and pap != 0 and sci != 0):
        winner = sci
    else:
        winner = len(rps)
    
    return winner


sum = 0
for i in range(m):
    winner = n
    count = 0

    while winner != 1:
        count += 1
        rps = RPS(winner)
        print(str(count) + " 번째  :  " + str(rps))
        winner = win(rps)

    print("\n RPS 횟수 : " + str(count))
    sum += count

print("\n\n< " + str(n) + "명이서 RPS " + str(m) + "회 실행시 평균 횟수 > \n" + str(sum / m))

