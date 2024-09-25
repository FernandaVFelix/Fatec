/* DEQUES (ou FILAS DUPLAS) */

class Deque {
    constructor() {
        this.count = 0; // Apontador para o fim da fila.
        this.lowestCount = 0; // Apontador para o início da fila.
        this.items = {}; //objeto
    }

    addFront(element) {
        if (this.isEmpty()) {
            this.addBack(element); // inserção de elementos na fila - adiciona só no final da fila
        }
        else {
            if (this.lowestCount > 0) {
                this.lowestCount--;
                this.items[this.lowestCount] = element;
            }
            else {
                for (let i = this.count; i > 0; i--) {
                    this.items[i - 1] = this.items[i];
                }
                count++;
                this.lowestCount = 0;
                this.items[0] = element;
            }
        }
    }

    addBack(element) { // inserção de elementos na fila - adiciona só no final da fila
        this.items[this.count] = element;
        this.count++;
    }

    removeFront() {   // remoção de elementos da fila 
        if (this.isEmpty()) {
            return undefined;
        }

        // Salva o primeiro elemento da fila, pois será removido.
        const result = this.items[this.lowestCount];
        delete this.items[this.lowestCount]; // Remove o primeiro elemento da fila

        this.lowestCount++; // não existe mais, pois foi removido.
        return result;
    }

    removeBack(){ // Remove o elemento da parte superior
        if(this.isEmpty()){
            return undefined;
        }
        // salva o último elemento da fila, pois será removido.
        const result = this.items[this.count-1];
        delete this.items[this.count-1];
        this.count--;
        return result;
    }

    // Dando uma espiada no primeiro elemento da fila.
    peekFront(){ // vendo o que está na frente da fila
        if(this.isEmpty()){
            return undefined;
        }
        return this.items[this.lowestCount];
    }

    peekBack(){ //Retorna o objeto na parte superior do Stack sem removê-lo
        if(this.isEmpty()){
            return undefined;
        }
        return this.items[this.count-1];
    }

    clear(){ //limando a fila
        this.items = {};
        this.count = 0;
        this;lowestCount = 0;
    }

    size(){ //verificando se a fila está vazia e qual seu tamanho
        return this.count - this.lowestCount;
    }

    isEmpty(){  // retorna true se a fila estiver vazia e false caso contrário
        return this.size() === 0;
    }

    toString(){ // criando o método toSting()
        if(this.isEmpty()){
            return '';
        }
        let objString = `${this.items[this.lowestCount]}`;
        for (let i = this.lowestCount + 1; i < this.count; i++){
            objString = `${objString},${this.items[i]}`;
        }
        return objString;
    }
}
    
// INSTANCIANDO
const deque = new Deque(); 
console.log("deque.isEmpty() --> ",deque.isEmpty()); // true

console.log("deque.size() -->",deque.size()); // 0 (zero)

deque.addBack("John");
deque.addBack("Jack");

console.log("deque.size() -->",deque.size());  // 2
console.log(deque.toString()); // John,Jack

deque.addBack("Camila");
console.log(deque.toString()); // John,Jack,Camila

console.log("deque.isEmpty() -->",deque.isEmpty()); // false

console.log("deque.size() -->",deque.size()); // 3

deque.removeFront(); // John foi removido

console.log(deque.toString()); // Jack,Camila

deque.removeBack(); // Camila saiu

console.log(deque.toString()); // Jack

deque.addFront("John"); // John entra de novo, no início da fila

console.log(deque.toString()); // John,Jack
