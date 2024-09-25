// CAIXA ELETRÔNICO

/* Em determinado momento do dia, apenas notas de 10, 50 e 100 estão disponíveis em um terminal de caixa eletrônico. 
Elaborar uma função em Javascript chamada sacar() que receba o valor de saque de um cliente, verifique sua validade 
(ou seja, se pode ser pago com as notas disponíveis) e informe o número mínimo de notas de 100, 50 e 10 necessárias para pagar esse saque. */

import promptSync from "prompt-sync"
const prompt = promptSync()

let valor = Number(prompt("Digite o valor que deseja sacar: "))

function sacar(valor) {
    if (valor % 10 !== 0) {
        return "Valor inválido. Insira um valor múltiplo de 10.";
    }

    let notas100 = 0;
    let notas50 = 0;
    let notas10 = 0;

    notas100 = Math.floor(valor / 100);
    valor = valor % 100;

    notas50 = Math.floor(valor / 50);
    valor = valor % 50;

    notas10 = Math.floor(valor / 10);

    return `Notas de 100: ${notas100}, Notas de 50: ${notas50}, Notas de 10: ${notas10}`   
}

console.log(sacar());