


def maximo(a, b, c):
    maiorValor = b

    if a < b < c or b < a < c:
        maiorValor = c 
    elif b < c < a or c < b < a:
        maiorValor = a


    
    return maiorValor

print(maximo(100, 350, 1001))

def teste():
    maximo(2, 6, -4) == 6

def teste1():
    maximo(1, 2, 3) == 3

def teste2():
    maximo(30, 14, 10) == 30

def teste3():
    maximo(0, -1, 1) == 1

def teste4():
    maximo(1, 5, 3) == 5