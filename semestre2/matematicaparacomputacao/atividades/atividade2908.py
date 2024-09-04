"""Dados dois conjuntos contendo 5 elementos ,cada conjunto. 
OBS: o conjunto (vetor) não deve conter elementos repetidos, para isso implemente o carregamento do vetor contendo elementos não repetidos. 
Calcule a união, intersecção, A-B, B-A, diferença simétrica e P(A). 
Apresentar os conjuntos A e B de forma classificada crescentemente. 
Para as operações acima, não apresente elemento repetido. 
Apresente a palavra VAZIO para quando o vetor de respostas não tiver elemento."""

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