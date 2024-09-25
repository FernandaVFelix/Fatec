<<<<<<< HEAD
// para rodar NPX TSC --> cria um arquivo js
// FUNÇÕES EM TYPESCRIPT

// npm i prompt-sync // npm i -D @types/prompt-sync

import PromptSync from 'prompt-sync'
const prompt = PromptSync()
=======
// npm i prompt-sync
// npm i -D @types/prompt-sync
>>>>>>> fcf422a449681aab81fcd33f97ad49de5cc26bde

/* FUNÇÕES EM TYPESCRIPT */

import PromptSync from 'prompt-sync'
const prompt = PromptSync()

function calcularArea(lado: number): number { // sempre tem que colocar o tipo da variavel
    return lado * lado
}

<<<<<<< HEAD
// opcional ==> let texto: String = ""
let texto = ""
texto = "10"

// const quadrado = calcularArea("b") --> não deixa passar pq passou como valor uma string e é number
const quadrado = calcularArea(2)  // const quadrado: number = calcularArea(2)
console.log(quadrado)


// INTERFACES: formas de definir contratos ou objetos
// configuração dos padroes de como os objetos de Aluno devem se comportar

type situacao = 'aprovado' | 'reprovado' // para travar status que não podem ser mudados durante o código

interface Aluno { // aqui também pode usar o type - não altera em nada
    nome: String,
    mediaFinal: number,
    situacao: situacao
}

// json de objetos
const aluno: Aluno = {
    nome: "Teste",
    mediaFinal: 3,
    situacao: "reprovado",
    // cpf: 0
}

// aluno.cpf = 300 // para criar assim um objeto tem que esta no json

const aluno2: Aluno = {
    nome: "Teste 2",
=======
const numDigitado = Number(prompt("Digite um num: "))

// const quadrado = calcularArea("b") --> não deixa passar pq passou como valor uma string e é number
const quadrado = calcularArea(numDigitado) // const quadrado: number = calcularArea(2)
console.log(quadrado)

type situacao = 'aprovado' | 'reprovado'
interface Aluno {
    nome: string
    mediaFinal: number
    situacao: situacao
}

const aluno: Aluno = {
    nome: "",
>>>>>>> fcf422a449681aab81fcd33f97ad49de5cc26bde
    mediaFinal: 9,
    situacao: "aprovado"
}

<<<<<<< HEAD
console.log(aluno.nome) // imprime só o nome do aluno, acessando metodos ou atributos
=======
const aluno2: Aluno = {
    nome: "Teste 2",
    mediaFinal: 0,
    situacao: "reprovado"
}
>>>>>>> fcf422a449681aab81fcd33f97ad49de5cc26bde

function alunoFactory(nome: string, mediaFinal: number): Aluno {
    let situacao: situacao = 'reprovado'
    if (mediaFinal > 6) {
        situacao = 'aprovado'
    }

<<<<<<< HEAD
    return { 
        nome: nome, // se tem o mesmo nome da variavel não precisa colocar duas vezes
=======
    return {
        nome: nome,
>>>>>>> fcf422a449681aab81fcd33f97ad49de5cc26bde
        mediaFinal,
        situacao
    }
}

<<<<<<< HEAD
const aluno3 = alunoFactory('Teste 3', 8)
=======
const aluno3 = alunoFactory('Teste 3', 9)
>>>>>>> fcf422a449681aab81fcd33f97ad49de5cc26bde
console.log(aluno3.situacao)