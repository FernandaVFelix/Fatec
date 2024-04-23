'''Exercício Fix25 - Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser 
pintada. Considere que a cobertura da tinta é de 1 litro para cada 
6 metros quadrados e que a tinta é vendida em latas de 18 litros, que 
custam R$80,00 ou em galões de 3,6 litros, que custam R$ 35,00. 
Informe ao usuário as quantidades de tinta a serem compradas e os 
respectivos preços em 3 situações:'''

import math

print("")
print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027")
print("")

tam = float(input("Informe o tamanho, em metros quadrados, da área a ser pintada: "))
opc = int(input("Para comprar apenas latas de 18 litros digite 1\n Para comprar apenas galões de 3,6 litros digite 2\n Para comprar ambos digite 3: "))
qntdtinta = 0
qntdlata = 0
qntdgalao = 0
preco = 0
acres = 0

if(opc == 1):
    qntdtinta = tam / 6
    qntdlata = qntdtinta / 18
    preco = qntdlata * 80
    print("A quantidade de tinta a ser comprada é: ", qntdlata, " latas de 18 litros")
    print("E o valor será: ", preco)
elif(opc == 2):
    qntdtinta = tam / 6
    qntdgalao = qntdtinta / 3.6
    preco = qntdgalao * 35
    print("A quantidade de tinta a ser comprada é: ", qntdgalao, " galões de 3,6 litros")
    print("E o valor será: ", preco)
elif(opc == 3):
    acres = tam + (tam * 0.10)
    qntdtinta = acres / 6
    qntdlata = int(qntdtinta / 18.0)
    qntdgalao = int((qntdtinta - (qntdlata * 18)) / 3.6)
    if (qntdtinta - (qntdlata * 18) % 3.6 != 0):
        qntdgalao += 1
    preco = (qntdgalao * 35) + (qntdlata * 80)
    print("A quantidade de tinta a ser comprada é: ", qntdgalao, " latas de 18 litros e ", qntdgalao, "galões de 3,6 litros")
    print("E o valor será: ", preco)