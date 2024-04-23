'''Exercício Fix35 - Altere o algoritmo anterior (Fix42) para que o usuário entre com a nota do exame. Lembre-se que deve se realizar a média aritmética entre a média e a nota do exame. O sistema deverá informar a ele as seguintes mensagens: 

a) Se a média for maior ou igual a cinco: Parabéns, você aproveitou a sua chance! Está aprovado. 

b) Se a média for menor que cinco: Estude mais para a próxima. Você não alcançou o mínimo necessário. '''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027") 
print("") 

nome = input("Digite seu nome: ") 
ra = int(input("Digite seu RA: ")) 
n1 = float(input("Digite sua primeira nota: ")) 
n2 = float(input("Digite sua segunda nota: ")) 
n3 = float(input("Digite a nota do exame: ")) 

def calcula_media(n1, n2):
     md = (n1 + n2) / 2
     return md

def calcula_media_final(n3):
     mdf = (calcula_media(n1, n2) + n3) / 2
     if(mdf >= 5): 
        print(nome, " sua média foi ", mdf, "Parabéns, você aproveitou a sua chance! Está aprovado")
        return mdf
     elif(mdf < 7): 
        print(nome, " sua média foi ", mdf, " Estude mais para a próxima. Você não alcançou o mínimo necessário.")
        return mdf

calcula_media_final(n3)