/* Considere uma pilha P vazia e uma fila F não vazia. Utizando
apenas os testes de fila e pilha vazias, as operações Enfileira, 
Desenfileira, Empilha, Desempilha, e uma varivael aux do TipoItem,
escreva uma função que inverta a ordem dos elementos da fila */

function inverteOrdem(fila) {
    let pilha = [];

    // Desenfileira e empilha todos os elementos
    while (fila.length > 0) {
        pilha.push(fila.shift());
    }

    // Desempilha e enfileira os elementos
    while (pilha.length > 0) {
        fila.push(pilha.pop());
    }
}

let fila = [1, 2, 3, 4, 5]; // lista aleatória
inverteOrdem(fila);
console.log(fila); // Imprime a lista invertida