// CONVERSOR DE TEMPERATURA

/* Crie uma função em JavaScript que converta uma temperatura de Celsius para Fahrenheit. 
A função deve:
Receber um parâmetro numérico representando a temperatura em Celsius Calcular a temperatura 
equivalente em Fahrenheit Retornar o resultado arredondado para uma casa decimal
Lembre-se que a fórmula para converter Celsius para Fahrenheit é: F = (C * 9/5) + 32 */

import promptSync from "prompt-sync"
const prompt = promptSync() 

let tempCelsius = Number(prompt('Digite a temperatura em celsius: '))

function conversor(tempCelsius) {
  const calculo = (tempCelsius * 9 / 5) + 32
  return calculo
}

console.log(conversor(tempCelsius))