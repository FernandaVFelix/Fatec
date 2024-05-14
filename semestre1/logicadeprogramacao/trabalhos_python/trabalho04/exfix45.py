'''Exercício Fix45 - Elaborar um algoritmo (programa) que determine se a pessoa está com no seu Peso Ideal (ou não) e IMC. 
Onde o usuário deverá digitar o peso, o sexo e a altura de uma determinada pessoa. Após a execução, 
deverá exibir se esta pessoa está ou não com seu peso ideal. Veja tabela (a) e (b) da relação peso/altura².
Incluir uma mensagem na qual deverá aparecer o seu nome, RA e turma antes do resultado final, depois faça um (printscreen) e 
comentar o(s) resultado(s) do programa após a execução do mesmo '''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027\n") 
print("Turma de Desenvolvimento de Software Multiplataformas - Fatec Indaiatuba - 2024") 
print("")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
sexo = int(input("Informe seu sexo: (Digite 1 para feminino e 2 para masculino)"))
imc = peso / (altura * altura)
    
if(sexo == 1):
    if(imc < 19):
        print("Você está abaixo do peso")
    elif(19 <= imc < 24):
        print("Você está no seu peso ideal")
    elif(imc > 24):
        print("Você está acima do peso")
elif(sexo == 2):
    if(imc < 20):
        print("Você está abaixo do peso")
    elif(20 <= imc < 25):
        print("Você está no seu peso ideal")
    elif(imc > 25):
        print("Você está acima do peso")