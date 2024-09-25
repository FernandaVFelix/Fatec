/* ESTRUTURA DE UMA LISTA LIGADA */
class LinkedList {
    constructor(equalsFn = defaultEquals) { // função de comparação
        this.count = 0; // armazena o numero de elementos da lista
        this.head = undefined; // primeiro elemento
        this.equalsFn = equalsFn; // comparação
    }

    /* PUSH */
    push(element) {
        const node = new Node(element); // cria um novo nó com valor element
        let current; // declara variavel
        if (this.head == null) { // verifica se ta vazio
            this.head = node;
        } else {
            current = this.head; // inicia a iteração pela lista
            while (current.next != null) { // vai até encontrar o ultimo nó
                current = current.next;
            }
            current.next = node; // o ultimo nó recebe um novo nó como proximo
        }
        this.count++; // incrementa todos elementos
    }

    /* REMOVEAT */
    removeAt(index) {
        if (index >= 0 && index < this.count) { // verifica se é valido
            let current = this.head; // inicia o head para iterar a lista
            if (index === 0) { // se o indice é 0 o primeiro ó é removido
                this.head = current.next;
            } else {
                let previous; // nó anterior ao que queremos remover
                for (let i = 0; i < index; i++) { // percorre a lista
                    previous = current; // armazena o nó anterior
                    current = current.next; // atualiza o nó
                }
                previous.next = current.next; // faz o nó anterior pular o nó atual e apontar para o próximo
            }
            this.count--; // decrementa o contador
            return current.element;
        }
        return undefined; // se for invalido
    }

    /* INSEERT */
    insert(element, index) {
        if (index >= 0 && index <= this.count) { // verifica se é valido
            const node = new Node(element);
            if (index === 0) { // se é 0 insere o elemento no comelo
                const current = this.head;
                node.next = current; // o novo nó aponta para o atual
                this.head = node; // atualiza o head para o novo nó
            } else {
                const previous = this.getElementAt(index - 1); // obtém o ó anterior à posição desejada
                const current = previous.next; // obtém o nó atual na posição onde o novo elemento será inserido
                node.next = current; // o novo nó aponta para o nó atual
                previous.next = node; // o nó anterior aponta para o novo nó
            }
            this.count++;
            return true;
        }
        return false; // seo indice for invalido retorna false
    }

}