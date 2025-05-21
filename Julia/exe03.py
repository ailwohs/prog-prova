'''3) Um usuário colocou 7 itens no seu carrinho de supermercado. Faça um algoritmo que o usuário irá
digitar o valor de cada um deste itens. Ao final, o programa deverá exibir na tela:
a) O item de maior valor
b) O item de menor valor
c) O somatório dos valores dos itens.'''

'''

#IMPLEMENTAÇÃO 2022

num=int(input("Digite o valor dos intens adicionados ao carrinho \t>"))
maior_valor=num
menor_valor=num 
soma=0 
for i in range(0,7):
    num = int(input("Digite o restante de itens: \t>"))
    if (num > maior_valor):
        maior_valor=num
    if (num < menor_valor):
        menor_valor=num
    soma=soma+num
print("O item de maior valor é:", maior_valor)
print("O item de menor valor é:", menor_valor)
print("A soma de todos os itens é:", soma)
'''

#IMPLEMENTAÇÃO 2025
num = float(input("Digite o valor dos itens adicionados ao carrinho \t>"))
maior_valor = num
menor_valor = num
soma = num

for i in range(0, 6):
    num = float(input("Digite o restante de itens: \t>"))
    if num > maior_valor:
        maior_valor = num
    if num < menor_valor:
        menor_valor = num
    soma = soma + num

print("O item de maior valor é:", maior_valor)
print("O item de menor valor é:", menor_valor)
print("A soma de todos os itens é:", soma)
