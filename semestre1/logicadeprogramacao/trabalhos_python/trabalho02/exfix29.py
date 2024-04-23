'''Exercício Fix29 Elabore  um programa em PYTHON, que mostre  os 
descontos  concedidos  pela  loja  ABC  em suas mercadorias. 
Em  compras  acima  de  R$  300,00  forneça  20%  de  desconto, 
entre  R$  200,00  a  R$  299,99 desconto de 10% e abaixo de R$ 199,99 
o desconto será de 5%. Mostre na tela o valor total e o valor final a
pagar (com o desconto). Solicite ao usuário que digite os valores 
via teclado.'''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027")
print("")

cp = float(input("Digite o valor da compra:"))
desc = 0

if(cp >= 300):
    desc = cp - (cp * 0.20)
    print("O valor total da sua compra é ", cp, " e com o desconto fica: ", desc)
elif((cp >= 200) & (cp <= 299.99)):
    desc = cp - (cp * 0.10)
    print("O valor total da sua compra é ", cp, " e com o desconto fica: ", desc)
elif(cp <= 199.99):
    desc = cp - (cp * 0.05)
    print("O valor total da sua compra é ", cp, " e com o desconto fica: ", desc)
else:
    print("Por favor, digite um valor existente")