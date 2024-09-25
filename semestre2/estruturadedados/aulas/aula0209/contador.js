// FILAS (Queues)

class Queue { // criando a classe Queue
    constructor() {
        // this.count = 0; // declarando a propriedade count
        // this.lowestCount = 0; // declara essa variavel para remover os elementos na frente da fila
        this.items = {}; // usando um objeto para armazenar os elementos
        this.head = 0;
        this.tail = 0;
    }

    // inserção de elementos na fila - adiciona só no final da fila
    enqueue(element) {
        this.items[this.tail] = element;
        this.tail++;
    }

    // remoção de elementos da fila 
    dequeue() {
        if (this.isEmpty()) {
            return undefined; // verifica se a fila está vazia se si retorna indefinido
        }

        // const result = this.items[this.lowestCount]; // se a fila tiver vazia o valor é armazenado na frente dela
        // delete this.items[this.lowestCount]; // remove o elemento
        // this.lowestCount++; // incremento de +1
        // return result; // devolve o vlaor
        
        
        const item = this.items[this.head];
        delete this.items[this.head];
        this.head++;
        return item;

    
    }

    // vendo o que está na frente da fila
    peek() {
        if (this.isEmpty()) {
            return undefined;
        }
        return this.items[this.head];
    }

    // verificando se a fila está vazia e qual seu tamanho
    size() {
        return this.count - this.lowestCount;
    }

    isEmpty() {
        return this.size() === 0; // retorna true se a fila estiver vazia e false caso contrário
    }

    // limando a fila - chama o método até resultar em indefinido ou apenas reinicia o valor das propriedades da classe
    clear() {
        this.items = [];
        this.count = 0;
        this.lowestCount = 0;
    }

    // criando o método toSting()
    toString() {
        if (this.isEmpty()) {
            return '';
        }
        let objString = `${this.items[this.lowestCount]}`;
        for (let i = this.lowestCount + 1; i < this.count; i++) {
            objString = `${objString}, ${this.items[i]}`;
        }
        return objString;
    }

    

}

const queue = new Queue();
console.log(queue.isEmpty()); // exibe true

// acrescenta elemento
queue.enqueue('Jack');
console.log(queue.toString()); // exibe Jhon, Jack

// acrescentando elementos
queue.enqueue('Camila')

console.log(queue.toString()); // Jhon, Jack, Camila
console.log(queue.size()); // exibe 3
console.log(queue.isEmpty()); // exibe false

// remove Jhon
queue.dequeue(); 

// remove Jack
queue.dequeue();

console.log(queue.toString()); // Camila
