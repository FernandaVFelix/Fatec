'''Exercício Fix22 - Faça um algoritmo que mostre os descontos 
concedidos pela loja ABC em suas mercadorias. Em compras acima de 300,00 
forneça 20% de desconto, para 200,00 desconto de 15% e acima de 100,00 
o desconto será de 10%. Atribua valores as variáveis compra1, compra2 e 
compra3. Mostre na tela o valor total e o valor com o devido desconto. 
Os mesmos devem ser solicitados ao usuário, digite os valores via teclado.'''

print("")
print("Programa desenvolvido por Fernanda Victória Felix Oliveira   RA:1051392411027")
print("")

cp1 = float(input("Digite o valor da primeira compra:"))
cp2 = float(input("Digite o valor da segunda compra:"))
cp3 = float(input("Digite o valor da terceira compra:"))
vt = cp1 + cp2 + cp3
desc1 = vt - (vt * 0.20)
desc2 = vt - (vt * 0.15)
desc3 = vt - (vt * 0.10)

if(vt > 300):
    print("O valor total da sua compra é ", vt, "e com o desconto fica: ", desc1)
elif(vt == 200):
    print("O valor total da sua compra é ", vt, "e com o desconto fica: ", desc2)
elif((vt > 100) & (vt < 200)):
    print("O valor total da sua compra é ", vt, "e com o desconto fica: ", desc3)
else:
    print("O valor total da sua compra é ", vt, "e nao possui desconto")