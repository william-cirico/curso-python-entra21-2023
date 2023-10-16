"use strict";

alert("Hello world!");

let birthYear = prompt("Em que ano você nasceu?");
let currentYear = prompt("Qual é o ano atual?", new Date().getFullYear());

let age = currentYear - birthYear;
console.log(age);

const isAdult = confirm("Você é maior de idade?");
if (isAdult) {
    console.log("Você pode dirigir");
} else {
    console.log("Você não pode dirigir");
}