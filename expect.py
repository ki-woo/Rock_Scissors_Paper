from fractions import Fraction

num = 20    ## 여기 있는 숫자 수정하면 됨 
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


for i in range(2, num+1):
    count.append(RSP(i))
    print("a" + str(i) + " : " + str(count[i-1]) + "     (" + str(float(count[i-1])) + ")")

