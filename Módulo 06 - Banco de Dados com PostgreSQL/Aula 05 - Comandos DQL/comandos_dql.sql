-- Selecionando todas as colunas de uma tabela
SELECT * FROM employees;

-- Selecionando colunas em específico de uma tabela
SELECT name, age FROM employees;

-- Definindo limite para a consulta
SELECT name, age FROM employees LIMIT 3;

-- Definindo início para a consulta
SELECT name, age FROM employees OFFSET 3 LIMIT 3;

-- Selecionando com condições (WHERE)
SELECT * FROM employees WHERE age > 30;

-- Between
SELECT * FROM employees WHERE age BETWEEN 20 AND 25;

-- Com o tipo money
SELECT * FROM employees WHERE salary BETWEEN 'R$ 3000' AND 'R$ 7000';

-- Cast -> Conversão de tipos
SELECT * FROM employees WHERE CAST(salary as numeric) BETWEEN 3000 AND 7000;

-- Operador de Cast (::)
SELECT * FROM employees WHERE salary::numeric BETWEEN 3000 AND 7000;

-- Operador IN
SELECT * FROM employees WHERE age IN (27, 29, 41);

-- Operador LIKE (case-sensitive)
SELECT * FROM employees WHERE name LIKE 'Igor%';

-- Operador ILIKE (case-insensitive)
SELECT * FROM employees WHERE name ILIKE 'igor%';

-- Usando o _
SELECT * FROM employees WHERE name ILIKE 'i___ %';

-- INNER JOIN
SELECT employees.name, departments.name 
FROM employees
INNER JOIN departments
ON employees.department_id = departments.id;

-- Usando apelidos para as colunas
SELECT employees.name Funcionário, departments.name Departamento
FROM employees
INNER JOIN departments
ON employees.department_id = departments.id;

-- Usando apelidos para as tabelas
SELECT e.name "Nome do funcionário", d.name "Nome do departamento"
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id;

-- LEFT JOIN
SELECT e.name Funcionário, d.name Departamento
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.id;

-- RIGHT JOIN
SELECT e.name Funcionário, d.name Departamento
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.id;

-- FULL JOIN
SELECT e.name Funcionário, d.name Departamento
FROM employees e
FULL JOIN departments d
ON e.department_id = d.id;

-- COUNT
SELECT COUNT(*) FROM employees;

-- SUM
SELECT SUM(salary) FROM employees;

-- MIN
SELECT MIN(salary) FROM employees;

-- MAX
SELECT MAX(salary) FROM employees;

-- AVG
SELECT AVG(salary::numeric) FROM employees;

-- ROUND
SELECT ROUND(AVG(salary::numeric), 2) FROM employees;

-- GROUP BY - Usar quando for selecionar uma função agregadora + outra coluna
SELECT department_id "ID do Departamento", COUNT(*) "Quantidade de Funcionários"
FROM employees
GROUP BY 1;

-- COALESCE - Verifica se a coluna possui valor, senão possuir mostra o valor padrão
SELECT 
	COALESCE(department_id::text, 'Funcionário sem departamento') "ID do Departamento",
	COUNT(*) "Quantidade de Funcionários"
FROM employees
GROUP BY 1;

-- Com LEFT JOIN - Por funcionário
SELECT
	COALESCE(d.name, 'Sem departamento') "Departamento",
	COUNT(*) "Quantidade de Funcionários"
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.id
GROUP BY 1;

-- Com RIGHT JOIN - Por departamento
SELECT
    d.name "Nome do Departamento",
    COUNT(e.department_id) "Quantidade de Funcionários"
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
GROUP BY 1;

-- DISTINCT - Remover duplicatas da consulta
SELECT DISTINCT(age)
FROM employees;

-- ORDER BY - Ordernar os valores da consulta
SELECT DISTINCT(age)
FROM employees
ORDER BY 1;

-- HAVING - Filtrar por uma função agregadora
SELECT
	department_id "ID do Departamento",
	COUNT(department_id) "Quantidade de Funcionários"
FROM employees
GROUP BY 1
HAVING COUNT(department_id) > 3;

-- Com INNER JOIN
SELECT
	COALESCE(d.name, 'Sem departamento') "Departamento",
	COUNT(e.department_id) "Quantidade de Funcionários"
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id
GROUP BY 1
HAVING COUNT(e.department_id) > 3;

-- Subconsultas -> Uma consulta que utiliza o resultado de outra consulta
SELECT name "Funcionário", salary "Salário"
FROM employees
WHERE salary::numeric > (SELECT AVG(salary::numeric) FROM employees);










