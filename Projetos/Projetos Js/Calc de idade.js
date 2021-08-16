const prompt = require('prompt-sync')();
const ano1 = prompt("Em qual ano você nasceu?  ");

let d = new Date();
let ano = d.getFullYear();
console.log(`o ano atual é ${ano}`);

let idade = ano - ano1;

let niver = prompt("Já fez aniverssário este ano ?") 
if(niver == "N" || niver == "n"){
    console.log(`você tem ${idade - 1} anos de idade`);
} else {
    console.log(`você tem ${idade} anos de idade`);

};

