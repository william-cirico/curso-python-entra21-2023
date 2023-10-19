"use strict";

alert("Hello world!");

const birthYear = prompt("Em que ano você nasceu?");
const currentYear = prompt("Qual é o ano atual?", new Date().getFullYear());

const age = currentYear - birthYear;
console.log(age);

const isAdult = confirm("Você é maior de idade?");
if (isAdult) {
    console.log("Você pode dirigir");
} else {
    console.log("Você não pode dirigir");
}