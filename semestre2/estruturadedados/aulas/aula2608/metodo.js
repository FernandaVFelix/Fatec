/* MÉTODOS */

let numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
numbers[numbers.length] = 10 // adiciona o valor na posição final do array (sem push)

/* ADICIONAR ELEMENTOS */
numbers.push(11) // adiciona o valor na posição final do array
numbers.push(12, 13)
numbers.unshift(-1) // adiciona o valor antes da primeira posição
numbers.unshift(-4, -3)

/* REMOVER ELEMENTOS */
numbers.pop() // remove o ultimo elemento
numbers.splice(5,3) // remove um elemento apartir da posição (posição, deleta 3 num)

console.log(numbers)
console.log(numbers.length)