'''Exercício Fix44 - Desenvolva um programa para determinar a média geral do aluno. 
O mesmo deverá receber o nome do aluno, as 2 notas obtidas do aluno nas 2 avaliações. 
Calcular a média de aproveitamento, usando a fórmula da Media e escrever o conceito do aluno de acordo com a tabela de conceitos.  
Média é dada pela fórmula: MG = (NP1*4 + NP2*6) / 10 '''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027\n") 
print("Turma de Desenvolvimento de Software Multiplataformas - Fatec Indaiatuba - 2024") 
print("")

nome = input("Digite o nome do aluno(a): ")
nota1 = float(input("Digite a nota recebida na primeira avaliação: "))
nota2 = float(input("Digite a nota recebida na segunda avaliação: "))

media = ((nota1*4) + (nota2*6)) / 10

if((media >= 9) and (media <= 10)):  
    print(nome, "seu conceito é A, e sua situação é: está Aprovado")  
elif((media >= 7) and (media < 9)):  
    print(nome, "seu conceito é B, e sua situação é: está Aprovado")  
elif((media >= 3) and (media < 7)):  
    print(nome, "seu conceito é C, e sua situação é: precisa do Exame")  
elif((media >= 0) and (media < 3)):  
    print(nome, "seu conceito é A, e sua situação é: está de DP") 