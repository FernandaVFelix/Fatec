// imprimindo algum valor
console.log('Olá Mundo')

// hoje não se usa mais var para criar variavel

// tipos de variaveis
const a = 10 // variavel constante que não pode ser alterada, numerica
let b = 20 // variavel mutavel
const c = "Teste" // string
const d = true // boolean
const e = null // null
const f = undefined // undefined
const g = Symbol() // symbol

// operação com as variaveis
const total = a + b

// imprimindo uma variavel
console.log(total)

// exemplo de if, else if e else
if(total >30){
    console.log('total > que 30')
}else if(total == 30){
    console.log('total = 30')
}else{
    console.log('total < que 30')
}

// exemplo de switch (toLowerCase() deixa tudo minusculo e toUpperCase() deixa tudo em capslock)
let dia = 'segunda'
switch(dia){
    case 'segunda':
        console.log('aberto')
        break;
    case 'sabado':
        console.log('fechado')
        break;
    default:
        console.log('meio aberto')
        break;
}

// operador ternário
let idade = 18
let podeBeber = idade >= 18 ? 'Pode beber' : 'Não pode beber'

// operador lógico (&& = and, || = or, ! = not)
const maiorIdade = true
const temCarteiraTrabalho = true
const podeAplicarVaga = maiorIdade && temCarteiraTrabalho
const canditadoNegado = !podeAplicarVaga

// exemplo de for
for (let i = 0; i <= 10; i++){
    console.log(i)
}

// exemplo while
let peso = 100
while(peso > 0.8){
    // o peso vai reduzir em 20% a cada iteração
    peso = peso * 0.8
    console.log(peso)
}

// exemplo do while
let totaL = 0
do{
    totaL = totaL + 1
    console.log(totaL)
}while(totaL < 10)


//usando impotação de biblioteca

//prompt com commonjs
//const prompt = require('prompt-sync')()

//prompt com module
import PromptSync from "prompt-sync"
const prompt = PromptSync()

let valor = Number(prompt('Digite o saldo inicial: '))
const acrescimo = Number(prompt('Digite o acrescimo: '))
const valorF = valor * 3
let meses = 0

 while(valor < valorF){
    valor = valor + (valor * acrescimo)
    meses = meses + 1
    console.log(meses)
}