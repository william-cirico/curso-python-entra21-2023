"use strict";

/**
 * Mostra uma mensagem no navegador.
 * @param {string} from  
 * @param {string} message 
 */
function showMessage(from, message = "Mensagem não fornecida") {
    alert(`${from}: ${message}`);
}

showMessage("William", "Declarando funções!");
showMessage("Unknown");

/**
 * Retorna a soma de dois números
 * @param {number} n1 
 * @param {number} n2 
 * @returns {number}
 */
function sum(n1, n2) {
    return n1 + n2;
}

console.log(sum(10, 2));

// Arrow functions
/**
 * Retorna o dobro de um número
 * @param {number} n 
 * @returns {number}
 */
const double = n => n * 2;
console.log(double(3));

// Multiline arrow function
/**
 * Retorna a subtração de um número por outro
 * @param {number} n1 
 * @param {number} n2 
 * @returns {number}
 */
const sub = (n1, n2) => {
    const result = n1 - n2;
    return result;
}