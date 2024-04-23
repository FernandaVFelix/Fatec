'''Exercício Fix30 Desenvolva um programa em Python que receba via teclado um valor e 
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