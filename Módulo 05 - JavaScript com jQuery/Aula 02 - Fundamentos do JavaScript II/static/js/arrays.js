// Criando um array
const colors = ["red", "green", "blue", "black", "white", "purple"];

// Tamanho do arary
console.log(colors.length);

// Adicionar elemento
colors.push("yellow");

// Remover último elemento
colors.pop();

// Remover um elemento pelo índice
colors.splice(1, 1);

// Fatiando o array
console.log(colors.slice(0, 2));

// Iterando em um array
for (let i = 0; i < colors.length; i++) {
    console.log(colors[i]);
}

for (let color of colors) {
    console.log(color);
}

colors.forEach((item, index, array) => {
    console.log(`${item} está no indice ${index} no vetor: ${array}`);
});

// Procurando índice do elemento
console.log(colors.indexOf("black"));

// Verificando se o elemento existe no vetor
console.log(colors.includes("yellow"));