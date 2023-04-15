num = int(input("Digite um número: "))



msg = "não"
numAnterior = num % 10
numAtual = num
tamanhoNum = len(str(num))
i = 0

if tamanhoNum != 1:
	while i < tamanhoNum:

		numAtual = numAtual // 10

		if numAtual % 10 == numAnterior:

			msg = "sim"
			break
		
		numAnterior = numAtual % 10
		i = i+1

print(msg)