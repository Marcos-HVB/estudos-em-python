

def partida():
    quantidadeDePecasN  
    limitePecasJogadaM
    pcJogou 


    while quantidadeDePecasN < 1 or limitePecasJogadaM < 1 or limitePecasJogadaM >= quantidadeDePecasN:
        quantidadeDePecasN   = int(input("Quantas peças? "))
        limitePecasJogadaM = int(input("Limite de peças por jogada? "))
    
    
    if quantidadeDePecasN % limitePecasJogadaM == 0:
        usuarioJogou = true
        print("Você começa!")

        quantidadeDePecasN -= usuario_escolhe_jogada(quantidadeDePecasN, limitePecasJogadaM)
    else:
        print("Computador começa!")
        pcJogou = false
        quantidadeDePecasN -= computador_escolhe_jogada(quantidadeDePecasN, limitePecasJogadaM)   

    while quantidadeDePecasN > 0:
        if pcJogou:
            usuario_escolhe_jogada(quantidadeDePecasN, limitePecasJogadaM)
        else:
            computador_escolhe_jogada(quantidadeDePecasN, limitePecasJogadaM)



def computador_escolhe_jogada(n, m):

    return escolhaComputador



def usuario_escolhe_jogada(n, m):
    escolhaJogador

    escolhaJogador = int(input("Informe sua jogada: "))

    if escolhaJogador > m or escolhaJogador < 1:
        while escolhaJogador > m or escolhaJogador < 1:
            escolhaJogador = int(input("Informe uma jogada válida jogada: "))

    

    return escolhaJogador


def campeonato():
    pontuacaoC = 0
    pontuacaoU = 0
    i = 0 
    while i < 3:
        print("**** Rodada", i,"****")
        partida()
        i += 1

    print("**** Final do campeonato! ****")
    print("Placar: Você",pontuacaoU, "X", pontuacaoC, "Computador")



# começa o programa
print("Bem vindo ao jogo do NIM! Escolha: ")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um capeonato")

escolha = int(input())

while escolha != 1 or escolha != 2:

    if escolha == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    elif escolha == 2:
        print("Você escolheu um campeonato!")
        campeonato()