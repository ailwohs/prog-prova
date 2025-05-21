'''4) A JFMudança está construindo uma calculadora para informar aos seus clientes o preço do seu
serviço. Para auxiliar na tarefa você deve construir um algoritmo onde o usuário informará a distância
a ser percorrida e o programa mostrará o valor final a ser cobrado. Para o cálculo, utilize como o
valor de R$3,50 por quilômetro rodado para distâncias inferiores a 20 km e R$2,50 para distâncias
maiores de 20 km. Independente da distância também deverá ser cobrado o valor de R$35,00 que
corresponde a taxa de serviço. O programa deverá rodar enquanto a distância for diferente de zero.'''
'''
num=int(input("Digite a distância a ser percorrida \t>"))
while num !=0:
 if num <=20:
  preço_km = 3.50
  preço_pagar = num * preço_km
  print("O valor a ser pago é:", preço_pagar)
 elif num >=20:
  preço1_km = 2.50
  preço1_pagar = num * preço1_km + 35.00
  print("O valor para pagar é de:", preço1_pagar)
 num=int(input("Digite zero para encerrar"))
#else:
    #print("Inválido")
 '''
 #a=num+3,50+35
 #b=num+2,50+35
 #if(num >=20 and a == <=10 and a== >=10):
 #if num (<=20):
  #   print("A valor a ser percorrido é:", num+3,50+35)
  

distancia = int(input("Digite a distância a ser percorrida (ou 0 para encerrar): "))

while distancia != 0:
    if distancia < 20:
        preco_km = 3.50
    else:
        preco_km = 2.50

    valor_total = distancia * preco_km + 35.00

    print("Distância informada:", distancia, "km")
    print("Valor total a ser pago: R$", valor_total)

    distancia = int(input("\nDigite a distância a ser percorrida (ou 0 para encerrar): "))
