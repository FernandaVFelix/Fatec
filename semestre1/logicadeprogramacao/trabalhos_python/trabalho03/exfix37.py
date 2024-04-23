'''Exercício Fix37 - Elabore um programa em PYTHON, que mostre os descontos concedidos pela loja ABC em
suas mercadorias. Em compras acima de R$ 300,00 forneça 20% de desconto, entre R$ 200,00 a R$ 299,99 
desconto de 10% e abaixo de R$ 199,99 o desconto será de 5%. Mostre na tela o valor total e o valor 
final a pagar (com o desconto). Solicite ao usuário que digite os valores via teclado. '''

print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027") 
print("") 

vt = float(input("Digite o valor total da compra:")) 

def desc1(vt):
    desc = vt - (vt * 0.20)
    print("O valor total da sua compra é ", vt, " e com o desconto fica: ", desc)
    return desc  

def desc2(vt):
    desc = vt - (vt * 0.10) 
    print("O valor total da sua compra é ", vt, " e com o desconto fica: ", desc) 
    return desc

def desc3(vt):
    desc = vt - (vt * 0.05) 
    print("O valor total da sua compra é ", vt, " e com o desconto fica: ", desc)

if(vt >= 300): 
    desc1(vt)
elif((vt >= 200) & (vt <= 299.99)): 
    desc2(vt)
elif(vt <= 199.99): 
     desc3(vt)
else: 
    print("Por favor, digite um valor existente")