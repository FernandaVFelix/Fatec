'''Exercício Fix26 Desenvolva um programa em Pythonque receba via 
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