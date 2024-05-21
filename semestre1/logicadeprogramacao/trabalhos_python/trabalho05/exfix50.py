'''Exercício Fix50 - Considere os arquivos mensagem.txt desenvolva um programa em Python e determine: 
a)O tamanho da variável(mensagem.text). Qual foi o método utilizado: 
b)Criar uma lista com as palavras encontradas no arquivo mensagem.text. Qual foi o método utilizado: '''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027\n")      
print("Turma de Desenvolvimento de Software Multiplataformas - Fatec Indaiatuba - 2024")      
print("")   

import os 
tam = os.path.getsize('mensagem.txt') 
print("Tamanho do conteúdo do arquivo: ", tam, "bytes")

print("")
print("")

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027\n")      
print("Turma de Desenvolvimento de Software Multiplataformas - Fatec Indaiatuba - 2024")      
print("")

arqv = open('mensagem.txt', 'r', encoding='utf-8')   
conteudo = arqv.read() 
palav = conteudo.split()
print("Palavras dentro do arquivo: \n ", palav) 
arqv.close()