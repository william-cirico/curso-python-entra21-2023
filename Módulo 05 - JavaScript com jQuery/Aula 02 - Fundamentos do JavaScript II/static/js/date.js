// Criando uma data
const now = new Date();

// Acessando partes da data
const year = now.getFullYear();
const month = now.getMonth() + 1;
const day = now.getDate();
const hours = now.getHours();
const minutes = now.getMinutes();
const seconds = now.getSeconds();
const dayOfWeek = now.getDay(); // 0 - Domingo à 6 (Sábado)
const timestamp = now.getTime(); // https://pt.wikipedia.org/wiki/Marca_temporal

// Modificando a data
now.setFullYear(2024);
now.setHours(10);
