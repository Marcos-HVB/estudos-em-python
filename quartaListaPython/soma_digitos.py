num = int(input("Digite um número inteiro: "))


i = 0 
numAtual = num
somaNumeros = 0
while i < len(str(num)):
    somaNumeros = somaNumeros + numAtual % 10    
    numAtual = numAtual // 10
    i = i + 1
    

print(somaNumeros)