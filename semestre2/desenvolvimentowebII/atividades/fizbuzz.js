/* Fizzbuzz

Escreva uma função chamada fizzbuzz que recebe um número inteiro positivo n como entrada e 
imprime os números de 1 a n, mas com as seguintes regras:
Se o número for divisível por 3, imprima "Fizz" em vez do número.
Se o número for divisível por 5, imprima "Buzz" em vez do número.
Se o número for divisível por ambos 3 e 5, imprima "FizzBuzz".
Caso contrário, imprima o próprio número.
Exemplos:

Exemplo 1: n = 5

1
2
Fizz
4
Buzz
        
Exemplo 2: n = 15

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz*/

import promptSync from "prompt-sync"
const prompt = promptSync()

let num = Number(prompt('Digite um número inteiro e positivo: '))

function fizzbuzz(num) {
    for (let i = 1; i <= num; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log("FizzBuzz");
        } else if (i % 3 === 0) {
            console.log("Fizz");
        } else if (i % 5 === 0) {
            console.log("Buzz");
        } else {
            console.log(i);
        }
    }
}

fizzbuzz(num);
console.log('---');