/* ARRAY (VETORES) */
// Pilhas tem como base os arrays
// Array = estrutura de dados mais simples possível em memória
// O array armazena uma lista de valores que são todos do mesmo tipo, sequencialmente

const averageTemp = [];   /* Criação do Array - só cria não imprime nada*/
averageTemp [0] = 31.9;
averageTemp [1] = 35.3;
averageTemp [2] = 42.4;
averageTemp [3] = 52;
averageTemp [4] = 60.8;


let daysOfWeek= []; // array vazio
let diasDaSemana = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

console.log(diasDaSemana.length) // .length = imprime o tamanho do vetor

for(let i = 0; i < diasDaSemana.length; i++){ 
    console.log(i, diasDaSemana[i]); // coloca a posição o array na frente do valor
}

console.log(diasDaSemana); // imprime o array como um todo




