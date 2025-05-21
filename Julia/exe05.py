'''5) A empresa de suco, CascaUva deseja saber quantos caminhões e engradados serão necessários
para transportar sua produção ao final de uma semana de trabalho. Construa um programa que fará
a leitura de quantas garrafas foram produzidas em cada dia da semana (segunda, terça, quarta,
quinta e sexta) e informe quantos caminhões e quantos engradados precisarão ser reservados para
o transporte. Cada caminhão tem capacidade para levar um máximo de 25 engradados que
comportam até 24 garrafas.'''


'''
#IMPLEMENTAÇÃO 2022

i=int(input("Produção de segunda \t>"))
for i in range (1,5):
    i=int(input("Digite a do resto da semana \t>"))
quant_cam= i= 25+1
quant_eng= i=25 + 24 
print("Serão necessários", quant_cam, "caminhões, e:", quant_eng , "engradados")

'''

# IMPLEMENTAÇÃO 2025
dias = ["segunda", "terça", "quarta", "quinta", "sexta"]
total_garrafas = 0

for dia in dias:
    producao = int(input("Digite a quantidade de garrafas produzidas na " + dia + "feira: "))
    total_garrafas += producao

garrafas_por_engr = 24
engr_por_caminhao = 25

total_engr = (total_garrafas + garrafas_por_engr - 1) // garrafas_por_engr
total_caminhoes = (total_engr + engr_por_caminhao - 1) // engr_por_caminhao

print("Total de garrafas:", total_garrafas)
print("Total de engradados necessários:", total_engr)
print("Total de caminhões necessários:", total_caminhoes)
