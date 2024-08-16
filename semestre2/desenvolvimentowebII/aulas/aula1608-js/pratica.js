// 1. Crie um código que vai receber um valor e uma porcentagem de acréscimo 
// ao mês, quantos meses são necessários para o valor triplicar? Exiba quantos 
// meses levaram para essa condição ocorrer.

let valor = 100
const acrescimo = valor * 0.2
const valorF = valor * 3
let meses = 0

 while(valor < valorF){
    valor = valor + acrescimo
    meses = meses + 1
    console.log(meses)
}

//1. Crie um código com Node que escreva a tabuada de um número digitado pelo usuário.
// A tabuada deve ser apresentada no console como:
// 1X2=2
// 2X2=4

import PromptSync from "prompt-sync"
const prompt = PromptSync()

let num = Number(prompt('Digite um número: '))
let tabuada = 0

for(let i = 0; i <=10; i++){
    tabuada = num * i
    console.log(`${i}X${num}=${tabuada}`)
}