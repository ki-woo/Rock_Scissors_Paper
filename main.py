from fractions import Fraction
import random as r

n = 10      # 참여자 수
m = 1000    # 시행 횟수


count = [0]

def combi(n, k):
    com = 1
    for i in range(n - k + 1, n + 1): # nPk
        com *= i
    
    for i in range(1, k + 1): # / k!
        com = Fraction(com, i)
    
    return com

def sigma(n):
    sig = 0
    for i in range(1, n):
        sig += combi(n, i) * count[i-1]
    
    return sig

def RSP(n): # x / y
    return Fraction(3 ** (n-1) + sigma(n), 2 ** n - 2)


for i in range(2, n+1):
    count.append(RSP(i))
    #print("a" + str(i) + " : " + str(count[i-1]) + "     (" + str(float(count[i-1])) + ")")

exp = count[n-1]

#================================
#================================

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

print("\n\n< " + str(n) + "명이서 가위바위보 " + str(m) + "회 실행시 평균 시행 횟수 > \n근사값 : " + str(sum / m))
print("기대값 : " + str(float(exp)) + " (" + str(exp) + ")")

