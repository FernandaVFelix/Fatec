'''Exercício Fix32 Elabore um programa em Python que o usuário entre com 
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