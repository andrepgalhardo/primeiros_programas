n = int(input("Digite um número natural: "))

fatorial = 1

for i in range(1, n+1):
    fatorial *= i

print(fatorial)
