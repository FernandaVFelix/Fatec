/* FUNÇÃO --> para "coisas" que acontecem mais de uma vez no código*/
/* não usar o var dentro da função - pode dar erro */

function somar(a,b){ /* entre parênteses são os parametros */
    const total = a + b
    // return total
    return Number(total) /* aqui força o resultado ser um número */
    /* return = sempre usar quando quiser devolver algum valor */
}

function calcular (a,b, operacao){
    const resultado =  operacao(a,b)
    console.log(resultado)
    return resultado
}

console.log(50)

console.log(calcular(20,30,somar))

// -> calcular a=20 e b=30 e operacao = fn somar()
// -> somar a=20 e b=30 e total=50


function imprimir(texto){
    console.log(texto) /* void - nao pode voltar como variável */ /* local */
}

const teste = somar(10,20) /* aqui deve passar o valor do paramêtro da função */
imprimir (teste)
// console.log(total) /* global */


// ATALHO DE FUNÇÕES
const atalho = console.log // atribui o valor da função para a variável
atalho("teste") 

const atalho2 = somar

function calcular(a,b,operacao){
    return operacao(a,b)
}

calcular(20,30,somar)

/* ARROW FUNCTION */ /* ambos fazem o mesmo */
const sub = (a,b) => { // aqui está em uma constante - como se fosse uma função anônima
    return a - b
}

/* function sub2(a,b){ // aqui está em uma função - se usar essa na hora de chamar o código será maior
    return a - b
} 

calcular (30,20, function sub(a,b){  --> aqui está chamando caso crie função
    //
})
*/

/* CHAMANDO UMA ARROW FUNCTION */
calcular (30, 20, (a,b) => { 
    //
})

// o arrow function pode fazer sem o return e sem parâmetros

