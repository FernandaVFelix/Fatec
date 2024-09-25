/* JOGO DA BATATA QUENTE */
// Funciona como uma Fila Circular 

// é necessário criar a classe deque com o constructor e com todos os métodos que são usados na função
class Deque {
    constructor() {
        this.count = 0; 
        this.lowestCount = 0;
        this.items = {}; 
    }

    addFront(element) {
        if (this.isEmpty()) {
            this.addBack(element);
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

    addBack(element) {
        this.items[this.count] = element;
        this.count++;
    }

    removeFront() { 
        if (this.isEmpty()) {
            return undefined;
        }

        const result = this.items[this.lowestCount];
        delete this.items[this.lowestCount]; 

        this.lowestCount++;
        return result;
    }

    removeBack(){ 
        if(this.isEmpty()){
            return undefined;
        }
        
        const result = this.items[this.count-1];
        delete this.items[this.count-1];
        this.count--;
        return result;
    }

    peekFront(){
        if(this.isEmpty()){
            return undefined;
        }
        return this.items[this.lowestCount];
    }

    peekBack(){
        if(this.isEmpty()){
            return undefined;
        }
        return this.items[this.count-1];
    }

    clear(){
        this.items = {};
        this.count = 0;
        this;lowestCount = 0;
    }

    size(){
        return this.count - this.lowestCount;
    }

    isEmpty(){ 
        return this.size() === 0;
    }

    toString(){
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

function hotPotato(elementsList, num) { // função fica fora da classe porém seus métodos estão todos definidos dentro da classe
    const deque = new Deque(); // usa uma Deque como fila, adicionando elementos apenas no final e retirando apenas no inicia
    const eliminatedList = [];

    for (let i = 0; i < elementsList.length; i++) {
        deque.addBack(elementsList[i]); // lista de nomes pré definida
    }

    while (deque.size() > 1) {
        for (let i = 0; i < num; i++) {
            deque.addBack(deque.removeFront()); // tiramos elementos do fim da fila e inserimos de volta no início da mesma fila
        }
        eliminatedList.push(deque.removeFront());
    }

    return {
        eliminated: eliminatedList,
        winner: deque.removeFront()
    };
}

const names = ['John', 'Jack', 'Camila', 'Ingrid', 'Carl'];
const result = hotPotato(names, 7);

result.eliminated.forEach(name => {
    console.log(`${name} foi eliminado do jogo de batata quente.`);
});

console.log(`O ganhador foi: ${result.winner}`);
