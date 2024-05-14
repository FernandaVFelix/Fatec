'''Exercício Fix45 - Desenvolva um programa que só permita o acesso a pessoas autorizadas (professor, via autenticação) 
para posteriormente realizar a média do aluno. Para isto Considere o programa criado no Fix44. 
Incluir uma mensagem na qual deverá aparecer o seu nome, RA e turma antes do resultado final, depois faça um (printscreen) e
 comentar o(s) resultado(s) do programa após a execução do mesmo. '''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027\n") 
print("Turma de Desenvolvimento de Software Multiplataformas - Fatec Indaiatuba - 2024") 
print("")

autent = int(input("Se você for professor digite 1, se for aluno digite 2, se for outro digite 3: "))

if(autent == 1):
    nome = input("Digite o nome do aluno(a): ")
    nota1 = float(input("Digite a nota recebida na primeira avaliação: "))
    nota2 = float(input("Digite a nota recebida na segunda avaliação: "))

    media = ((nota1*4) + (nota2*6)) / 10

    if((media >= 9) and (media <= 10)):  
        print("O conceito de", nome, " é A, e sua situação é: está Aprovado")  
    elif((media >= 7) and (media < 9)):  
        print("O conceito de", nome, " é B, e sua situação é: está Aprovado")  
    elif((media >= 3) and (media < 7)):  
        print("O conceito de", nome, " é C, e sua situação é: precisa do Exame")  
    elif((media >= 0) and (media < 3)):  
        print("O conceito de ", nome, " é A, e sua situação é: está de DP")
else:
    print("Você não tem permissão para utilizar esse programa.")