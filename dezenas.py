numeroInt = input('Digite um número inteiro: ')
num = int(numeroInt)

num1 = num / 100
num2 = (((num1 % 1) * 10) // 1)
print('O dígito das dezenas é : ', num2)
