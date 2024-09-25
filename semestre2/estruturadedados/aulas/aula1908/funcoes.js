// sintaxe básica de um função
function sayHello() {
    console.log('Hello!');
}

sayHello(); // chamando a função


// função com argumentos
// Argumentos são variáveis com as quais se supõe que a função fará algo
function output(text) {
    console.log(text);
}

// chamando a função e passando o valor dos argumentos
output('Hello!');
output('Hello!', 'Other text');


// nessa função o primeiro argumento será usado pela função; o segundo será ignorado
function sum(num1, num2) {
    return num1 + num2;
}

// a função calcula a soma de dois números e retorna o valor 
var result = sum(1, 2);
output(result); // a saída é 3