meuCartao = int(input("Digite o número do seu cartão de crédito: "))

cartaoLido = 1
encontreiMeuCartaoNaLista = False

while cartaoLido != 0 and not encontreiMeuCartaoNaLista:
    cartaoLido = int(input("Digite do próximo cartão de crédito: "))
    if cartaoLido == meuCartao:
        encontreiMeuCartaoNaLista = True
 
if encontreiMeuCartaoNaLista:
     print("EBA!!! Meu cartão está lá!")
else:
     print("XI!!! Meu cartão não está lá!")    
