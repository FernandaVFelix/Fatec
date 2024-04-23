'''Exercício Fix41 – O usuário deve digitar seu nome e sua idade. O sistema deverá informar as seguintes mensagens: 

Bem vindo NOME você é maior de idade. 

Bem vindo NOME você é menor de idade. 

Bem vindo NOME você é maior de 65 anos. '''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027") 
print("") 

nome = input("Informe seu nome: ")
idade = int(input("Agora informe sua idade (apenas com números): "))

def mensagem(nome, idade):
    if((idade >= 18) and (idade <= 65)):
        print("Bem vindo", nome, ", você é maior de idade.")
    elif(idade > 65):
        print("Bem vindo", nome, ", você é maior de 65 anos.")
    else:
        print("Bem vindo", nome, ", você é menor de idade.")

mensagem(nome, idade)