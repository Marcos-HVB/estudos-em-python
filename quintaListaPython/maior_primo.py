

def maior_primo(num):
    qtdDivisoes = 0
    contador2 = 1
    maiorPrimo = 0
    i = 1

    if num >=2:
        while i <= num:
            qtdDivisoes = 0
            contador2 = 1
         
            while contador2 <= i:

                if i % contador2 == 0:
                    qtdDivisoes += 1

                if qtdDivisoes > 2:
                    print("N é primo: ", i)
                    break
                
                contador2 += 1
            i += 1
            if qtdDivisoes == 2:
                print("validação se é primo")
                maiorPrimo = i - 1
    return maiorPrimo



def teste_maior_primo():
    assert maior_primo(100) == 97

def  teste_maior_primo2():
    assert maior_primo(7) == 7

def  teste_maior_primo3():
    assert maior_primo(5) == 5

def  teste_maior_primo24():
    assert maior_primo(55) == 53