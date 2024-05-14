'''Exercício Fix42 – Elabore um programa em Python que o usuário entre com seu e seu salário. Se o salário for menor ou igual a R$1500,00 
coloque um acréscimo de 20% de aumento. Se for maior que R$1500,00 e menor que R$2500,00 o acréscimo será de 10%, senão o acréscimo será de 
5% para os demais valores.'''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027\n") 
print("Turma de Desenvolvimento de Software Multiplataformas - Fatec Indaiatuba - 2024") 
print("") 

nome = input("Digite seu nome: ") 
sal = float(input("Digite seu salário: "))
print("") 

def calculo_aumento(sal):
    if(sal <= 1500.00):
        novsal = (sal * 0.20) + sal
        print(nome, "seu salário terá um aumento de 20% e sairá de: ", sal, " para: ", novsal)
        return novsal
    elif((sal > 1500) & (sal < 2500)): 
        acres = sal * 0.20 
        novsal = (sal * 0.10) + sal
        print(nome, "seu salário terá um aumento de 10% e sairá de: ", sal, " para: ", novsal)
        return novsal 
    else: 
        novsal = (sal * 0.05) + sal 
        print(nome, "seu salário terá um aumento de 5% e sairá de: ", sal, " para: ", novsal)
        return novsal

calculo_aumento(sal)