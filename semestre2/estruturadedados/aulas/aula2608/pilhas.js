/* PILHAS */

// LIFO = Last in Firt out - o ultimo a entrar o primeiro a sair

// {1} --> criou o constructor e adicionou um array vazio
class Stack {
    constructor() {
        this.items = [];
    }

    push(element) {
        this.items.push(element);
    }

    pop() {
        return this.items.pop();
    }

    peek() {
        return this.items[this.items.length - 1];
    }


    isEmpty() {
        return this.items.length === 0;
    }


    size() {
        return this.items.length;
    }

    clear() {
        this.items = [];
    }

}

// Exercício de Pilha: Codifique um conversor de decimal para binário
function decimalBinario(decNumer) {
    const remStack = new Stack();
    let number = decNumer;
    let rem;
    let binaryString = '';

    while (number > 0 ) {
        rem = Math.floor(number % 2);
        remStack.push(rem);
        number = Math.floor(number / 2);
    }
    while (!remStack.isEmpty()) {
        binaryString += remStack.pop().toString();
    }
    return binaryString;
}

console.log(decimalBinario(233))
console.log(decimalBinario(10))
console.log(decimalBinario(1000))
console.log(decimalBinario(1234))
console.log(decimalBinario(987))