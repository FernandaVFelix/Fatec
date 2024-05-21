'''Exercício Fix48 - Considere os arquivos email.txt desenvolva um programa em Python que cadastre mais 3 E-MAIL'''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027\n")    
print("Turma de Desenvolvimento de Software Multiplataformas - Fatec Indaiatuba - 2024")    
print("") 

arqv = open('email.txt', 'r', encoding='utf-8') 
lista = arqv.readlines() 

print("Digite novos e-mails para adicionar ao arquivo!") 

for _ in range(3):  
    lista = [email.split()[0] for email in lista] 
    novo_email = input("Digite um e-mail: ") 
    lista.append(novo_email) 
    print("Email adicionado!") 

print(lista) 
arqv.close() 