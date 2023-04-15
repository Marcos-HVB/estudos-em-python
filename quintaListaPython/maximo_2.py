



def maximo(a, b):
    maximo = a

    if(a < b):
        maximo = b

    return maximo

def teste_maior1():
    assert maximo(3, 4) == 4

def teste_maior2():
    assert maximo(0, -1) == 0

