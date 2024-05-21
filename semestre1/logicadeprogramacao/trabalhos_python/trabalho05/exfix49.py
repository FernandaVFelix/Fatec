'''Exercício Fix49 - Considere os arquivos senha.txt desenvolva um programa em Python que cadastre mais 5 senhas '''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027\n")     
print("Turma de Desenvolvimento de Software Multiplataformas - Fatec Indaiatuba - 2024")     
print("")  

arqv = open('senha.txt', 'r', encoding='utf-8')  
lista = arqv.readlines()  

print("Digite novas senhas para adicionar ao arquivo!")  

for _ in range(5):  
    lista = [senha.split()[0] for senha in lista]  
    novaSenha = input("Digite uma senha: ")  
    lista.append(novaSenha)  
    print("Senha adicionada!")  

print(lista)  
arqv.close() 