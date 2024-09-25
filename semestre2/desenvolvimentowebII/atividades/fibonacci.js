/*Fibonacci

Por definição, os dois primeiros números na sequência de Fibonacci são 0 e 1, e cada número 
subsequente é a soma dos dois anteriores.

Por exemplo, os primeiros dez números de Fibonacci são:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34

Escreva uma função que aceite um número e retorne o número naquela posição na sequência de Fibonacci.
Exemplos de saída:
console.log(fibonacci(3)); // Saída: 2 console.log(fibonacci(7)); // Saída: 13 console.log(fibonacci(9)); 
// Saída: 34 */

import promptSync from "prompt-sync"
const prompt = promptSync()

let num = Number(prompt('Digite um número inteiro: '))

function fibonacci(num) {
    if (num < 0) {
        throw new Error("O índice deve ser um número inteiro não negativo.");
    }

    if (num === 0) return 0;
    if (num === 1) return 1;

    let a = 0, b = 1, fibo = 1;

    for (let i = 2; i <= num; i++) {
        fibo = a + b; 
        a = b; 
        b = fibo; 
    }

    return fibo;
}

console.log(fibonacci(num));