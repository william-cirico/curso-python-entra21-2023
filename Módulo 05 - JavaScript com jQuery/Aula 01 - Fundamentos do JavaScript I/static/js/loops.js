// WHILE
let i = 0;
while (i < 3) {
    console.log(i);
    i++;
}

// FOR (começo; condição; passo)
for (let i = 0; i < 3; i++) {
    console.log(i);
}

// BREAK
let sum = 0;
while (true) {
    const value = +prompt("Digite um número");
    
    if (!value) break;

    sum += value;
}

console.log(`Soma: ${sum}`);

// CONTINUE
for (let i = 0; i < 3; i++) {
    if (i % 2 === 0) continue;

    console.log(i);
}