num = int(input("Digite um número inteiro: "))

msg = "Primo"
i = 1
qtdDivisoes = 0

while i <= num:
    if num % i == 0:
        qtdDivisoes += 1

    if qtdDivisoes > 2:
        msg = "Não primo"
        break 

    i += 1

print(msg)
