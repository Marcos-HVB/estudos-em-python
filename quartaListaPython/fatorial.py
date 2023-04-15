num = int(input("Digite o valor de n: "))

i = num - 1
result = 1 

if num != 0:
    while(i > 0):
        num = num * i
        i = i -1
    result = num

print(result)

