import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c


if delta < 0:
	print("Está equação não possui raizes reais")
else:
	raiz1 = -b + math.sqrt(delta) / (2 * a) 
	if delta == 0:
		print("A única raiz é:", raiz1)
	else:
		raiz2 = -b - math.sqrt(delta) / (2 * a)

		if raiz1 < raiz2:
			num1 = raiz1
			num2 = raiz2
		else:
			num1 = raiz2
			num2 = raiz1
		
		print("As raízes da equação são", num1,"e",num2)

	