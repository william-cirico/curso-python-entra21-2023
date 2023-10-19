"use strict";

let number = 1.23;
let string = "Hello World!";
let boolean = true;
let nothing = null;
let notDefined;

console.log(typeof number);
console.log(typeof string);
console.log(typeof boolean);
console.log(typeof nothing);
console.log(typeof notDefined);

// Type conversions
console.log(typeof String(1.23));
console.log(typeof Number("2"));
console.log(typeof +"2");