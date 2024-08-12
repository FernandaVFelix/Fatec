//alguns tipos de variaveis
var num = 1; // {1}
num = 3; // {2}
var price = 1.5; // {3}
var myName = 'Fernanda'; // {4}
var trueValue = true; // {5}
var nullVar = null; // {6}
var und; // {7}

//faz rodar no console do navegador
console.log('num: ' + num);
console.log('myName: ' + myName);
console.log('trueValue: ' + trueValue);
console.log('price: ' + price);
console.log('nullVar: ' + nullVar);
console.log('und: ' + und);

//declarar e atribuir valores as variaveis
var myVariable = 'global';
myOtherVariable = 'global';

//função
function myFunction() {
var myVariable = 'local';
return myVariable;
}
function myOtherFunction() {
myOtherVariable = 'local';
return myOtherVariable;
}

//faz rodar no console do navegador
console.log(myVariable); //{1}
console.log(myFunction()); //{2}
console.log(myOtherVariable); //{3}
console.log(myOtherFunction()); //{4}
console.log(myOtherVariable); //{5}