'''Exercício Fix43 - Elaborar um algoritmo (programa) que calcule o valor fatorial de um número inteiro positivo. 
Utilize a estrutura de controle for...in . Cálculo do fatorial, exemplo: fatorial de 5 = 5!=1x2x3x4x5= 120 '''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027\n") 
print("Turma de Desenvolvimento de Software Multiplataformas - Fatec Indaiatuba - 2024") 
print("")

valor = int(input("digite um número inteiro, positivo: "))
fatorial = 1

for n in range(1, valor+1):
    fatorial *= n
    
print("O fatorial do número digitado é: ", fatorial)