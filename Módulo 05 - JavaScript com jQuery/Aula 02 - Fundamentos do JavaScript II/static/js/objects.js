// Criando um objeto
const user = {
    name: "Will",
    age: 23
}; 

// Acessando os valores
console.log(user.name);
console.log(user["age"]);

// Obter os valores
console.log(Object.values(user));

// Obter as chaves
console.log(Object.keys(user));

// Obter as chaves e valores
console.log(Object.entries(user));
