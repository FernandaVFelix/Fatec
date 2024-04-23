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