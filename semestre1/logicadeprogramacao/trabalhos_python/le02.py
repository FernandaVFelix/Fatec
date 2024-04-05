'''Exercício Fix21- Faça um algoritmo com três variáveis numéricas 
(tipo int) que realize a média aritmética da multiplicação desses 3 
valores. Mostre os resultados na tela. Os mesmos devem ser solicitados 
ao usuário, digite os valores via teclado.'''

print("")
print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027")
print("")

n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))
n3 = int(input("Digite o último número:"))
media = (n1*n2*n3)/3

print("A média aritmética dos números digitados é", media)

'''Exercício Fix22 - Faça um algoritmo que mostre os descontos 
concedidos pela loja ABC em suas mercadorias. Em compras acima de 300,00 
forneça 20% de desconto, para 200,00 desconto de 15% e acima de 100,00 
o desconto será de 10%. Atribua valores as variáveis compra1, compra2 e 
compra3. Mostre na tela o valor total e o valor com o devido desconto. 
Os mesmos devem ser solicitados ao usuário, digite os valores via teclado.'''

print("")
print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027")
print("")
cp1 = float(input("Digite o valor da primeira compra:"))
cp2 = float(input("Digite o valor da segunda compra:"))
cp3 = float(input("Digite o valor da terceira compra:"))
vt = cp1 + cp2 + cp3
desc1 = vt - (vt * 0.20)
desc2 = vt - (vt * 0.15)
desc3 = vt - (vt * 0.10)


if(vt > 300):
    print("O valor total da sua compra é ", vt, "e com o desconto fica: ", desc1)
elif(vt == 200):
    print("O valor total da sua compra é ", vt, "e com o desconto fica: ", desc2)
elif((vt > 100) & (vt < 200)):
    print("O valor total da sua compra é ", vt, "e com o desconto fica: ", desc3)
else:
    print("O valor total da sua compra é ", vt, "e nao possui desconto")

'''Exercício Fix23 - Faça um algoritmo com duas variáveis numéricas 
(tipo int) que realize as 4 operações básicas (soma, subtração, 
multiplicação e divisão), mostre os resultados na tela. Os mesmos devem 
ser solicitados ao usuário, digite os valores via teclado.'''


print("")
print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027")
print("")

soma = 0
mult = 0
div = 0
sub = 0
n1 = int(input("Digite um número:"))
n2 = int(input("Digite mais um número:"))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2


print("A soma desses números é: ", soma)
print("A subtração desses números é: ", sub)
print("A multiplicação desses números é: ", mult)
print("A divisão desses números é: ", div)

'''Exercício Fix24 - Tendo como dado de entrada a altura (h) de uma pessoa,
 construa um algoritmo que calcule seu peso (p) ideal, utilizando as 
 seguintes fórmulas:Para homens: (72.7*h) -58
 Para mulheres: (62.1*h)-44.7'''

print("")
print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027")
print("")

gen = int(input("Se voce for uma mulher digite 1, se for um homem digite 2: "))
h = float(input("Digite sua altura: "))
p = 0

if(gen == 1):
    p = (62.1 * h) - 44.7
    print("O seu peso ideal é: ", p)
elif(gen == 2):
    p = float((72.7*h) -58)
    print("O seu peso ideal é: ", p)
else:
    print("Erro! Informe um genero válido '1' ou '2'")

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
