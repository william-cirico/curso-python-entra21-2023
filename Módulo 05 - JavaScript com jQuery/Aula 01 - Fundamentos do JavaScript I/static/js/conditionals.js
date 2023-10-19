"use strict";

let age = prompt("Quantos anos o JavaScript possui?");

if (age === 27) {
    console.log("Você acertou!");
} else if (age > 27) {
    console.log("A idade digitada é maior");
} else {
    console.log("A idade digitada é menor");
}

let myAge = 23;
let allowedAccess = (myAge >= 18) ? true : false;
console.log(allowedAccess);

// Strict Equality
console.log(0 == false); // true
console.log("" == false); //true

console.log(0 === false); // false
console.log("" === false); // false

// || (OR)
const currentHour = new Date().getHours();
if (currentHour < 8 || currentHour > 18) {
    console.log("O escritório está fechado!");
} else {
    console.log("O escritório está aberto!");
}

// && (AND)
if (currentHour > 7 && currentHour < 19) {
    console.log("O escritório está aberto!");
} else {
    console.log("O escritório está fechado!");
}

// ! (NOT)
console.log(!true);

const currentMonth = new Date().getMonth();


switch (currentMonth) {
    case 0:
        console.log("Janeiro");
        break;
    case 1:
        console.log("Fevereiro");
        break;
    case 2:
        console.log("Março");
        break;
    case 3:
        console.log("Abril");
        break;
    case 4:
        console.log("Maio");
        break;
    case 5: 
        console.log("Junho");
        break;
    case 6:
    case 7:
    case 8:
    case 9:
    case 10:
    case 11:
        console.log("Outros meses");
        break;
    default:
        console.log("Mês inválido!");
        break;
}