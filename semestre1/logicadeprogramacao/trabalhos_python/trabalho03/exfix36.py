'''Exercício Fix36 - Desenvolva um programa em Python que receba via teclado um valor e a partir disso faça: 

se o valor for1 e 2, mostre o valor elevado ao cubo; 

se o valor for múltiplo de 3 mostre o fatorial desse número; 

se o valor for 4,5,7 ou 8, mostre o valor dividido por 9. Caso não seja nenhum dos valores, informe como “valor inválido”. 
'''

import math

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027") 
print("") 

num = int(input("Digite um número inteiro:"))
mult3 = num % 3 

def cubo(num):
     pot = pow(num, 3)
     print("O número ", num, "elevado ao cubo fica: ", pot)
     return pot

def calcu_fat(num):
        fat = math.factorial(num)
        print("O fatorial do número ", num, "é", fat)
        return fat

def divisao(num):
     div = num / 9
     print("A divisão do número ", num, "por 9 é ", div)
     return div

if((num == 1) or (num == 2)): 
    cubo(num)
elif(mult3 == 0):
    calcu_fat(num)
elif((num == 4) or (num == 5) or (num == 7) or (num == 8)): 
    divisao(num)   
else: 
    print("O número ", num, " é inválido")