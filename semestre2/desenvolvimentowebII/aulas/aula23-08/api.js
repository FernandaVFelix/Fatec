// um contrato de serviço entre duas aplicações
// lugar onde tem dados e o código faz as requisições

// não atualiza automático

import express from 'express'

const app = express()
const port = 3000
app.use(express.json())

app.get('/',(requisicao,resposta) => {
    resposta.send('Olá Mundo') // devolve em mesnsagem simples
})

app.get('/teste',(requisicao,resposta) => {
    resposta.json({msg: "Teste1, teste2 ... "}) // devolve em json
})

// node api.js - rodar a api
app.listen(port, () => {
    console.log(`API rodando em http://localhost:${port}`)
})

// EXERCÍCIO PRÁTICO - Tabuada em "api" automatizada com número fixo
app.get('/tabuada',(requisicao,resposta) => {
    const numero = 2
    let tabuadaPronta = ''
    for(let i = 1; i <=10; i++){
        tabuadaPronta += `<p> ${numero} x ${i} = ${numero * i} <br>`  
    } 
    resposta.send(tabuadaPronta)
})