'''Exercício Fix31 Desenvolva um programa em Pythonque receba via 
tecladoum valor e a partir disso faça:
(1) se o valor for 1, 2 ou 3, mostre o valor elevado ao quadrado;
(2) se o valor for o número 4 ou 9, mostre a raiz quadrada do número; 
(3) se for os valores 6, 7 e 8, mostre o valor dividido 9.'''

import math

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027")
print("")

num = int(input("Digite um número inteiro:"))
ope = 0

if((num == 1) or (num == 2) or (num == 3)):
    ope = num ** 2
    print("O número ", num, "elevado ao quadrado fica: ", ope)
elif((num == 4) or (num == 9)):
    ope = math. sqrt(num)
    print("A raiz quadrada do número ", num, "é ", ope)
elif((num == 6) or (num == 7) or (num == 8)):
    ope = num / 9
    print("A divisão do número ", num, "por 9 é ", ope)
else:
    print("O número ", num, " não possui nenhuma operação disponível")


'''Exercício Fix32 Faça um algoritmo que calcule a média do aluno. 
Ele deve entrar com seu nome, ra, nota 1 e nota 2. 
O sistema deverá informar a ele as seguintes mensagens:
a)Se a média for maior ou igual a sete: Parabéns, você está aprovado!
b)Se  a média  for  menor  que  sete:  Você  ainda  tem  uma  chance!  
Estude  mais  para  o exame.'''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027")
print("")
nome = input("Digite seu nome: ")
ra = int(input("Digite seu RA: "))
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1 + n2) / 2

if(media >= 7):
    print(nome, " sua média foi ", media, "Parabéns, você está aprovado!")
elif(media < 7):
    print(nome, " sua média foi ", media, "Você  ainda  tem  uma  chance! Estude  mais  para  o exame.")


'''Exercício Fix33 Altere o algoritmo anterior (Fix32) para que o usuário 
entre com a nota do exame. Lembre-se que deve se realizar a média 
aritmética entre a média e a nota do exame. O sistema deverá informar 
a ele as seguintes mensagens:
a)Se a média for maior ou igual a cinco: Parabéns, você aproveitou a sua 
chance! Está aprovado.
b)Se a média for menor que cinco: Estude mais para a próxima. 
Você não alcançou o mínimo necessário.'''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027")
print("")
nome = input("Digite seu nome: ")
ra = int(input("Digite seu RA: "))
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("Digite a nota do exame: "))
media = (n1 + n2) / 2
mf = (media + n3) / 2

if(mf >= 5):
    print(nome, "Sua média foi ", mf, "Parabéns, você aproveitou a sua chance! Está aprovado")
elif(mf < 5):
    print(nome, "Sua média foi ", mf, " Estude mais para a próxima. Você não alcançou o mínimo necessário.")


'''Exercício Fix34 Elabore  um programa em PYTHON, que mostre  os 
descontos  concedidos  pela  loja  ABC  em suas mercadorias. 
Em  compras  acima  de  R$  300,00  forneça  20%  de  desconto, 
entre  R$  200,00  a  R$  299,99 desconto de 10% e abaixo de R$ 199,99 
o desconto será de 5%. Mostre na tela o valor total e o valor final a
pagar (com o desconto). Solicite ao usuário que digite os valores 
via teclado.'''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027")
print("")
cp = float(input("Digite o valor da compra:"))
desc = 0

if(cp >= 300):
    desc = cp - (cp * 0.20)
    print("O valor total da sua compra é ", cp, " e com o desconto fica: ", desc)
elif((cp >= 200) & (cp <= 299.99)):
    desc = cp - (cp * 0.10)
    print("O valor total da sua compra é ", cp, " e com o desconto fica: ", desc)
elif(cp <= 199.99):
    desc = cp - (cp * 0.05)
    print("O valor total da sua compra é ", cp, " e com o desconto fica: ", desc)
else:
    print("Por favor, digite um valor existente")


'''Exercício Fix35 Desenvolva um programa em Python que receba via teclado um valor e 
a partir disso faça:
(1)se for um valor negativo, mostre o módulo (valor sem sinal) do valor;
(2)se for um valor maior do que 10, solicite outro valor e mostre a 
diferença entre eles;
(3)Caso o valor não seja de nenhuma condição anterior, mostre o valor
dividido por 5'''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027")
print("")
num = int(input("Digite um número inteiro: "))
num2 = 0
mod = 0
dife = 0
div = 0

if(num < 0):
    mod = num % num
    print("O módulo do número ", num, "é: ", mod)
elif(num > 10):
    num2 = int(input("Digite mais um número: "))
    dife = num - num2
    print("A diferença entre os números digitados é: ", dife)
else:
    div = num / 5
    print("O resultado da divisão de ", num, " por 5 é: ", div) 



'''Exercício Fix36 Nesse programa o usuário deve entrar com um número e 
o sistema retornar se ele é divisível por 10 ou se é divisível por 5 ou 
se é divisível por 2, caso contrário retornar que o valor não é divisível
por nenhum desses valores.'''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027")
print("")
num = int(input("Digite um número inteiro: "))
div10 = num % 10
div5 = num % 5
div2 = num % 2

if((div10 == 0) & (div5 == 0) & (div2 == 0)):
    print("O número ", num, " é divisível por 10, por 5 e por 2")
elif(div5 == 0):
    print("O número ", num, " é divisível por 5")
elif(div2 == 0):
    print("O número ", num, " é divisível por 2")
else:
    print("O número ", num, " não é divisível nem por 10, nem por 5 e nem por 2")


'''Exercício Fix37 Elabore um programa em Python que o usuário entre com 
seu e seu salário. Se o salário for menor  ou  igual  a  R$1500,00  
coloque  um  acréscimo  de  20%  de  aumento.  Se  for  maior  que 
R$1500,00 e menor que R$2500,00 o acréscimo será de 10%, senão o 
acréscimo será de 5% para os demais valores.'''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027")
print("")
nome = input("Digite seu nome: ")
sal = float(input("Digite seu salário: "))
acres = 0
novsal = 0

if(sal <= 1500):
    acres = sal * 0.20
    novsal = sal + acres
    print(nome, "seu salário terá um aumento de 20% (", acres, "), saindo de: ", sal, " para: ", novsal)
elif((sal > 1500) & (sal < 2500)):
    acres = sal * 0.20
    novsal = sal + acres
    print(nome, "seu salário terá um aumento de 10% (", acres, "), saindo de: ", sal, " para: ", novsal)
else:
    acres = sal * 0.05
    novsal = sal + acres
    print(nome, "seu salário terá um aumento de 5% (", acres, "), saindo de: ", sal, " para: ", novsal)
