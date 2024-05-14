'''Exercício Fix44 - Elaborar um algoritmo (programa) que leia as notas de 5 alunos e retorne a maior nota da turma. 
Utilize a estrutura de controle while. '''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027\n") 
print("Turma de Desenvolvimento de Software Multiplataformas - Fatec Indaiatuba - 2024") 
print("")

nota1= float(input("Digite a nota do primeiro aluno(a): "))
nota2= float(input("Digite a nota do segundo aluno(a): "))
nota3= float(input("Digite a nota do terceiro aluno(a): "))
nota4= float(input("Digite a nota do quarto aluno(a): "))
nota5= float(input("Digite a nota do quinto aluno(a): "))

def maior(nota1, nota2, nota3, nota4, nota5):
               notaM = 0
               if((nota1 > nota2) and (nota1 > nota3) and (nota1 > nota4) and (nota1 > nota5)):
                    notaM = nota1
                    print("A maior nota é: ", notaM)
                    return notaM
               elif((nota2 > nota1) and (nota2 > nota3) and (nota2 > nota4) and (nota2 > nota5)):
                    notaM = nota2
                    print("A maior nota é: ", notaM)
                    return notaM
               elif((nota3 > nota1) and (nota3 > nota2) and (nota3 > nota4) and (nota3 > nota5)):
                    notaM = nota3
                    print("A maior nota é: ", notaM)
                    return notaM
               elif((nota4 > nota1) and (nota4 > nota2) and (nota4 > nota3) and (nota4 > nota5)):
                    notaM = nota4
                    print("A maior nota é: ", notaM)
                    return notaM
               else:
                    notaM = nota5
                    print("A maior nota é: ", notaM)
                    return notaM

def confereNota(nota1, nota2, nota3, nota4, nota5):
    if((nota1 > 10) or (nota2 > 10) or (nota3 > 10) or (nota4 > 10) or (nota5 > 10)):
     print("Este valor é inválido! Favor inserir uma nota de 0 a 10")
     return confereNota
    else:
     notas = True
     while (notas == True):
          maior(nota1, nota2, nota3, nota4, nota5)
          break
     
confereNota(nota1, nota2, nota3, nota4, nota5)
      