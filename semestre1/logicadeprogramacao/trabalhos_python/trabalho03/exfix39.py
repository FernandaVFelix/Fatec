'''Exercício Fix39 – Nesse programa o usuário deve entrar com um número e o sistema retornar se ele é divisível por 10 ou se é divisível 
por 5 ou se é divisível por 2, caso contrário retornar que o valor não é divisível por nenhum desses valores. '''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027") 
print("") 

num = int(input("Digite um número inteiro: ")) 

def divisoes(num):
    if((num % 10 == 0) and (num % 5 == 0) and (num % 2 == 0)):
        print("O número ", num, " é divisível por 10, por 5 e por 2")
        return num
    elif(num % 5 == 0):
        print("O número ", num, " é divisível por 5")
        return num
    elif(num % 2 == 0):
        print("O número ", num, " é divisível por 2")
        return num
    else:
        print("O número ", num, " não é divisível nem por 10, nem por 5 e nem por 2") 
        return num
    
divisoes(num)