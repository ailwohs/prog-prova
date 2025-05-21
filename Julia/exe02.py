'''2) Faça um algoritmo que solicite ao usuário o valor de uma mercadoria, O programa deverá calcular
o preço final dessa mercadoria, e apresentar os diversos valores conforme as formas de pagamento.
a) Para o valor a vista, deverá ser calculado com 10% de desconto,
b) A prazo em 2 vezes, deverá ser calculado com 5% de acréscimo,
c) A prazo em 3 vezes, deverá ser calculado com 6% de acréscimo,
d) A prazo em 4 vezes, deverá ser calculado com 7% de acréscimo,
e) A prazo em 5 vezes, deverá ser calculado com 9% de acréscimo.
Ao final, exiba todas as opções com seus respectivos valores. Para os valores a prazo, exibir o preço
original, o valor da parcela e também o preço final.'''

'''

n=float(input("Digite o valor da mercadoria \t>"))
print("O valor da mercadoria é:", n)
print("O valor a vista é:", n*90/100)
print("O preço da mercadoria é de:", n , "No prazo de 2x fica:", n*5)
print("O preço da mercadoria é de:", n , "No prazo de 3x fica:", n*6)
print("O preço da mercadoria é de:", n , "No prazo de 4x fica:", n*7)
print("O preço da mercadoria é de:", n , "No prazo de 5x fica:", n*9)
'''

'''num=int(input("Digite o valor da mercadoria\t>")
print("O valor da mercadoria é" , num)
print("O valor a vista é:", num*90/100)
print("O preço da mercadoria é de:", num , "No prazo de 2x fica:", num*5)
print("O preço da mercadoria é de:", num , "No prazo de 3x fica:", num*6)
print("O preço da mercadoria é de:", num , "No prazo de 4x fica:", num*7)
print("O preço da mercadoria é de:", num , "No prazo de 5x fica:", num*9)'''

#print("O valor do produto:", num , "Divitido em 2 vezes fica:", num*0,5)
#desconto=10
#valor_do_desconto = num * desconto / 100
#a_pagar = preço - valor_do_desconto'''

n=float(input("Digite o valor da mercadoria \t>"))

print("O valor da mercadoria é:", n)
print("O valor à vista (10% de desconto) é:", n * 0.90)
print("O preço da mercadoria é de:", n, "No prazo de 2x fica:", n * 1.05, "- Parcelas de:", (n * 1.05) / 2)
print("O preço da mercadoria é de:", n, "No prazo de 3x fica:", n * 1.06, "- Parcelas de:", (n * 1.06) / 3)
print("O preço da mercadoria é de:", n, "No prazo de 4x fica:", n * 1.07, "- Parcelas de:", (n * 1.07) / 4)
print("O preço da mercadoria é de:", n, "No prazo de 5x fica:", n * 1.09, "- Parcelas de:", (n * 1.09) / 5)
