const prompt = require('prompt-sync')();
const line = "*"
console.log(line.repeat(40));
console.log("Calculadora Simples");
console.log(line.repeat(40));
let p = prompt("Primeiro número.   ");
let s = prompt("segundo número.    ");
let pn = parseInt(p);
let sn = parseInt(s);
let sl = prompt("Qual o Sinal? Ex:[add] [sub] [mul] [div]   ");
switch(sl){
  case "add":
    console.log(`oi`);
    break;
  case "sub":
    console.log(`${pn} - ${sn} = ${pn-sn}`);
    break;
  case "mul":
    console.log(`${pn} * ${sn} = ${pn*sn}`);
    break;
  case "div":
    console.log(`${pn} ÷ ${sn} = ${Math.round(pn/sn)}`);
    break;
  default:
    console.log(`Por Favor coloque inputs válidos.`)
} 
//ele faz um grupo de ifs
//  o case seria tipo: em caso de 
//ai vc usa break pra parar o switch
//ai entre o break e o switch vc coloca oq
//vc quer que o codigo faça
//`${pn} + ${sn} = ${pn+sn}`