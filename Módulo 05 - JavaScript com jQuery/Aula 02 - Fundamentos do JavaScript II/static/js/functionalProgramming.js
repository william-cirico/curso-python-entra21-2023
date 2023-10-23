const people = [{
        name: "João",
        age: 19
    },
    {
        name: "Maria",
        age: 16
    },
    {
        name: "Paulo",
        age: 21
    },
];

const peopleNames = people.map(person => person.name);
const minors = people.filter(person => person.age < 18);
const sumOfAges = people.reduce((sum, person) => sum + person.age, 0);

// Para ordenar é necessário utilizar o slice() ou o destructuring, pois o sort() modifica o vetor em si.
const peopleOrderedByAge = [...people].sort((a, b) => a.age - b.age);

console.log(people);
console.log(peopleOrderedByAge);