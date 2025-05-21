'''1) Crie um algoritmo onde o usuário deverá digitar um numeral de 1 a 7. Para cada valor, o programa
deverá retornar o dia da semana (ex: se o usuário digitou 1, deverá retornar “Domingo”). Se o usuário
digitar 0 (zero) o programa deverá encerrar. Se o usuário digitar algo fora deste escopo, o programa
deverá retornar uma mensagem que foi digitada uma opção incorreta.'''

num = input("Digite um número de 1 a 7 \t>")
while num != "0":
    if num == "1":
        print("Domingo")
    elif num == "2":
        print("Segunda")
    elif num == "3":
        print("Terça")
    elif num == "4":
        print("Quarta")
    elif num == "5":
        print("Quinta")
    elif num == "6":
        print("Sexta")
    elif num == "7":
        print("Sábado")
    else:
        print("Opção incorreta")
    num = input("Digite um número de 1 a 7 ou zero (0) para encerrar\t>")

