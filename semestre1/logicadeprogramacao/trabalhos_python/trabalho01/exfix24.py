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