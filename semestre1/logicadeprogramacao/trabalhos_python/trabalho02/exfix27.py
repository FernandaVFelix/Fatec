'''Exercício Fix27 Faça um algoritmo que calcule a média do aluno. 
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