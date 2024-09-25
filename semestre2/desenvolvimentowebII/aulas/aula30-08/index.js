"use strict";
// npm i prompt-sync
// npm i -D @types/prompt-sync
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
/* FUNÇÕES EM TYPESCRIPT */
const prompt_sync_1 = __importDefault(require("prompt-sync"));
const prompt = (0, prompt_sync_1.default)();
function calcularArea(lado) {
    return lado * lado;
}
const numDigitado = Number(prompt("Digite um num: "));
// const quadrado = calcularArea("b") --> não deixa passar pq passou como valor uma string e é number
const quadrado = calcularArea(numDigitado); // const quadrado: number = calcularArea(2)
console.log(quadrado);
const aluno = {
    nome: "",
    mediaFinal: 9,
    situacao: "aprovado"
};
const aluno2 = {
    nome: "Teste 2",
    mediaFinal: 0,
    situacao: "reprovado"
};
function alunoFactory(nome, mediaFinal) {
    let situacao = 'reprovado';
    if (mediaFinal > 6) {
        situacao = 'aprovado';
    }
    return {
        nome: nome,
        mediaFinal,
        situacao
    };
}
const aluno3 = alunoFactory('Teste 3', 9);
console.log(aluno3.situacao);