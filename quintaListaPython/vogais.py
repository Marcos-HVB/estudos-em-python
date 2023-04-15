

def vogal(letra):

    letra = letra.lower()
    eVogal = letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"

    return eVogal


def teste_vogal():
    assert vogal("a") == True

def teste_vogal2():
    assert vogal("b") == False

def teste_vogal3():
    assert vogal("u") == True

def teste_vogal4():
    assert vogal("f") == False