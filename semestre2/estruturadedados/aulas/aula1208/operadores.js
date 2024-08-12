//variavel declarada
var num = 0; // {1}

//variavel com as operações
num = num + 2;
num = num * 3;
num = num / 2;

//operadores que adicionam ou subtraem direto do valor inserido na variavel
num++;
num--;

//operador que atribui a operação
num += 1; // {2}
num -= 2;
num *= 3;
num /= 2;
num %= 3;

//operadores de comparação
console.log('num == 1 : ' + (num == 1)); // {3}
console.log('num === 1 : ' + (num === 1));
console.log('num != 1 : ' + (num != 1));
console.log('num > 1 : ' + (num > 1));
console.log('num < 1 : ' + (num < 1));
console.log('num >= 1 : ' + (num >= 1));
console.log('num <= 1 : ' + (num <= 1));

//operadores lógico
console.log('true && false : ' + (true && false)); // {4}
console.log('true || false : ' + (true || false));
console.log('!true : ' + (!true));