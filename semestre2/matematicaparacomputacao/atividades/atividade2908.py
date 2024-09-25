"""Dados dois conjuntos contendo 5 elementos ,cada conjunto. 
OBS: o conjunto (vetor) não deve conter elementos repetidos, para isso implemente o carregamento do vetor contendo elementos não repetidos. 
Calcule a união, intersecção, A-B, B-A, diferença simétrica e P(A). 
Apresentar os conjuntos A e B de forma classificada crescentemente. 
Para as operações acima, não apresente elemento repetido. 
Apresente a palavra VAZIO para quando o vetor de respostas não tiver elemento."""

'''Com função'''

nomeA = "conjuntoA"
nomeB = "conjuntoB"

def conjuntoA(nomeA):
    vetorA = []
    print(f"Digite 5 elementos para o conjunto {nomeA}")
    while len(vetorA) < 5:
        elemento = int(input(f"\nElemento {len(vetorA) + 1}: "))
        if elemento not in vetorA:
            vetorA.append(elemento)
        else:
            print("\nElemento repetido, insira outro.")
    return sorted(vetorA)

def conjuntoB(nomeB):
    vetorB = []
    print(f"Digite 5 elementos para o conjunto {nomeB}")
    while len(vetorB) < 5:
        elemento = int(input(f"\nElemento {len(vetorB) + 1}: "))
        if elemento not in vetorB:
            vetorB.append(elemento)
        else:
            print("\nElemento repetido, insira outro.")
    return sorted(vetorB)

conjunto_a = conjuntoA(nomeA)
conjunto_b = conjuntoB(nomeB)

def uniao(conjunto_a, conjunto_b):
    return sorted(list(set(conjunto_a) | set(conjunto_b)))

def intersecao(conjunto_a, conjunto_b):
    return sorted(list(set(conjunto_a) & set(conjunto_b)))

def diferenca(conjunto_a, conjunto_b):
    return sorted(list(set(conjunto_a) - set(conjunto_b)))

def diferenca_simetrica(conjunto_a, conjunto_b):
    return sorted(list(set(conjunto_a) ^ set(conjunto_b)))

def partes_conjuntoA(conjunto_a):
    from itertools import chain, combinations
    return list(chain.from_iterable(combinations(conjunto_a, r) for r in range(len(conjunto_a) + 1)))

def imprimir_conjunto(nomeA, conjunto_a):
    if conjunto_a:
        print(f"\n{nomeA}: {conjunto_a}")
    else:
        print(f"\n{nomeA}: VAZIO")

uniao_result = uniao(conjunto_a, conjunto_b)
intersecao_result = intersecao(conjunto_a, conjunto_b)
a_menos_b_result = diferenca(conjunto_a, conjunto_b)
b_menos_a_result = diferenca(conjunto_b, conjunto_a)
diferenca_simetrica_result = diferenca_simetrica(conjunto_a, conjunto_b)
partes_a_result = partes_conjuntoA(conjunto_a)

imprimir_conjunto("Conjunto A", conjunto_a)
imprimir_conjunto("Conjunto B", conjunto_b)
imprimir_conjunto("A ∪ B", uniao_result)
imprimir_conjunto("A ∩ B", intersecao_result)
imprimir_conjunto("A - B", a_menos_b_result)
imprimir_conjunto("B - A", b_menos_a_result)
imprimir_conjunto("A ∆ B", diferenca_simetrica_result)
print(f"\nP(A): {partes_a_result}")

'''Sem função'''

from itertools import chain, combinations

nomeA = "conjuntoA"
nomeB = "conjuntoB"

vetorA = [] # vetor vazio para armazenar o conjunto
print(f"\n--> Digite 5 elementos para o {nomeA}: ")
while len(vetorA) < 5: # pede para o usuario inserir elementos até fechar 5 elementos
    elemento = int(input(f"\nElemento {len(vetorA) + 1}: ")) # pede para o usuario inserir os elementos
    if elemento not in vetorA: # verifica se o elemento iserido já está ou não no conjunto
        vetorA.append(elemento)
    else:
        print("\nElemento repetido, insira outro.")
conjunto_a = sorted(vetorA) # ordena o conjunto e armazena em conjunto_a


vetorB = []
print(f"\n--> Digite 5 elementos para o {nomeB}: ")
while len(vetorB) < 5:
    elemento = int(input(f"\nElemento {len(vetorB) + 1}: "))
    if elemento not in vetorB:
        vetorB.append(elemento)
    else:
        print("\nElemento repetido, insira outro.")
conjunto_b = sorted(vetorB)

uniao_result = sorted(list(set(conjunto_a) | set(conjunto_b)))
intersecao_result = sorted(list(set(conjunto_a) & set(conjunto_b)))
a_menos_b_result = sorted(list(set(conjunto_a) - set(conjunto_b)))
b_menos_a_result = sorted(list(set(conjunto_b) - set(conjunto_a)))
diferenca_simetrica_result = sorted(list(set(conjunto_a) ^ set(conjunto_b)))
partes_a_result = list(chain.from_iterable(combinations(conjunto_a, r) for r in range(len(conjunto_a) + 1)))

print (f"\n--> Resposta: ") 
if conjunto_a: 
    print(f"\nConjunto A: {conjunto_a}") 
else:
    print(f"\nConjunto A: VAZIO") 

if conjunto_b:
    print(f"\nConjunto B: {conjunto_b}")
else:
    print(f"\nConjunto B: VAZIO")

if uniao_result:
    print(f"\nA ∪ B: {uniao_result}")
else:
    print(f"\nA ∪ B: VAZIO")

if intersecao_result:
    print(f"\nA ∩ B: {intersecao_result}")
else:
    print(f"\nA ∩ B: VAZIO")

if a_menos_b_result:
    print(f"\nA - B: {a_menos_b_result}")
else:
    print(f"\nA - B: VAZIO")

if b_menos_a_result:
    print(f"\nB - A: {b_menos_a_result}")
else:
    print(f"\nB - A: VAZIO")

if diferenca_simetrica_result:
    print(f"\nA ∆ B: {diferenca_simetrica_result}")
else:
    print(f"\nA ∆ B: VAZIO")

print(f"\nP(A): {partes_a_result}")