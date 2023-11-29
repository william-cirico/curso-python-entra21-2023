-- 1)

-- a) Selecione o título e o autor de todos os livros.
SELECT title, author FROM books;

-- b) Selecione os livros escritos por Henry Davis.
SELECT * FROM books WHERE author ILIKE 'henry davis';

-- c) Selecione o título, autor e ano dos livros publicados antes de 1900.
SELECT title, author, release_year 
FROM books
WHERE release_year < 1900;

-- d) Selecione todos os livros cujo título comece com a letra "O".
SELECT * FROM books WHERE title ILIKE 'o%';

-- e) Selecione o título e o autor dos livros cujo ano seja posterior a 1950.
SELECT title, author FROM books WHERE release_year > 1950;

-- f) Selecione o número total de livros na tabela.
SELECT COUNT(*) FROM books;

-- g) Selecione o autor com o maior número de livros publicados.
SELECT author, COUNT(*)
FROM books
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;

-- h) Selecione os livros ordenados por ano em ordem ascendente.
SELECT * FROM books ORDER BY release_year;

-- i) Selecione o título do livro mais antigo.
SELECT title, release_year
FROM books
ORDER BY release_year 
LIMIT 1;

-- j) Selecione o título do livro mais recente.
SELECT title, release_year
FROM books
ORDER BY release_year DESC
LIMIT 1;

-- k) Selecione o título e o autor dos três últimos livros na tabela.
SELECT id, title, author
FROM books
ORDER BY id DESC
LIMIT 3;

-- 2)

-- a)Selecione a quantidade total de produtos em estoque.
SELECT SUM(quantity_in_stock) FROM products;

-- b) Selecione o preço médio dos produtos.
SELECT ROUND(AVG(price::numeric), 2) FROM products;

-- c) Selecione o produto mais caro da tabela.
SELECT * FROM products ORDER BY price DESC LIMIT 1;

-- d) Selecione o produto mais barato da tabela.
SELECT * FROM products ORDER BY price LIMIT 1;

-- e) Selecione o valor do total do estoque (preço * estoque) para cada produto.
SELECT product, price * quantity_in_stock "Valor total do estoque"
FROM products;

-- f) Selecione a quantidade de produtos que possuem estoque menor que 20.
SELECT COUNT(*)
FROM products
WHERE quantity_in_stock < 20;

-- g) Selecione o produto com o maior retorno após a venda de todas as unidades em estoque.
SELECT product, price * quantity_in_stock "Retorno das vendas"
FROM products
ORDER BY 2 DESC
LIMIT 1;

-- 3)

-- a) Selecione o nome e cargo de cada funcionário, juntamente com o departamento em que trabalham.
SELECT e.name funcionário, e.role cargo, d.name departamento
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id;

-- b) Selecione o nome, o cargo e o salário dos funcionários do departamento de vendas.
SELECT e.id, e.name funcionário, e.role, e.salary
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id
WHERE d.name ILIKE 'vendas';

-- c) Selecione o nome, o cargo e o salário dos funcionários cujo salário seja maior que 3500 e que trabalham no departamento de vendas.
SELECT e.name, e.role, e.salary
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id
WHERE e.salary::numeric > 3500 AND d.name ILIKE 'vendas';

-- d) Selecione o nome, o cargo, o salário e o nome do projeto associado a cada funcionário.
SELECT 
	e.name funcionário, 
	e.role, 
	e.salary, 
	STRING_AGG(p.name, ', ') projetos
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id
INNER JOIN projects p
ON p.department_id = d.id
GROUP BY e.id;

-- e) Liste o total gasto pela empresa no pagamento dos funcionários.
SELECT SUM(salary) FROM employees;

-- f) Liste o total de salário pago para os funcionários de cada departamento.
SELECT d.name departamento, SUM(e.salary)
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id
GROUP BY d.id;

-- g) Liste o maior salário de cada departamento.
SELECT d.name departamento, MAX(e.salary)
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id
GROUP BY d.id;

-- 4) 

-- a)Listar todos os alimentos e as suas respectivas categorias.
SELECT f.name alimento, c.name categoria
FROM foods f
INNER JOIN categories c
ON f.category_id = c.id;

-- b) Encontre o total de calorias para cada categoria de alimento.
SELECT c.name categoria, SUM(ni.calories)
FROM nutritional_information ni
INNER JOIN foods f
ON ni.food_id = f.id
INNER JOIN categories c
ON f.category_id = c.id
GROUP BY c.id;

-- c) Listar as dietas que incluem alimentos com mais de 500 calorias.
SELECT d.name dieta, STRING_AGG(f.name, ', ') alimentos
FROM diets d
INNER JOIN diets_foods df
ON df.diet_id = d.id
INNER JOIN foods f
ON df.food_id = f.id
INNER JOIN nutritional_information ni
ON ni.food_id = f.id
WHERE ni.calories > 500
GROUP BY d.id;

-- d) Calcular a média de proteínas por categoria de alimento.
SELECT c.name categoria, ROUND(AVG(ni.proteins), 2)
FROM categories c
INNER JOIN foods f
ON f.category_id = c.id
INNER JOIN nutritional_information ni
ON ni.food_id = f.id
GROUP BY c.id;

-- e) Identificar os alimentos que têm um teor de gordura superior à média de gordura de todos os alimentos.
SELECT f.name, ni.fats
FROM foods f
INNER JOIN nutritional_information ni
ON ni.food_id = f.id
WHERE ni.fats > (SELECT AVG(fats) FROM nutritional_information);

-- f) Listar as três categorias de alimentos com o maior número de itens.
SELECT c.name, COUNT(f.id)
FROM foods f
INNER JOIN categories c
ON f.category_id = c.id
GROUP BY c.id
ORDER BY 2 DESC
LIMIT 3;

-- g) Encontrar a dieta que tem o menor teor total de carboidratos.
SELECT d.name, SUM(ni.carbohydrates) "total de carboidratos"
FROM diets d
INNER JOIN diets_foods df
ON df.diet_id = d.id
INNER JOIN foods f
ON df.food_id = f.id
INNER JOIN nutritional_information ni
ON ni.food_id = f.id
GROUP BY d.id
ORDER BY 2
LIMIT 1;

-- h) Listar todos os alimentos que não estão incluídos em nenhuma dieta.
SELECT name FROM foods WHERE id NOT IN (SELECT food_id FROM diets_foods);

-- Consulta mais rápida em tabelas com muitos dados
SELECT f.name
FROM foods f
LEFT JOIN diets_foods df ON f.id = df.food_id
WHERE df.diet_id IS NULL;

-- i) Determinar a proporção de proteínas, carboidratos e gorduras (em porcentagem de calorias fornecidas) de cada alimento.
SELECT 
    f.name,
    ROUND((ni.proteins * 4 / (ni.proteins * 4 + ni.carbohydrates * 4 + ni.fats * 9)) * 100, 2) AS protein_percentage,
    ROUND((ni.carbohydrates * 4 / (ni.proteins * 4 + ni.carbohydrates * 4 + ni.fats * 9)) * 100, 2) AS carbohydrate_percentage,
    ROUND((ni.fats * 9 / (ni.proteins * 4 + ni.carbohydrates * 4 + ni.fats * 9)) * 100, 2) AS fat_percentage
FROM foods f
INNER JOIN nutritional_information ni 
ON f.id = ni.food_id;
	
-- Usando subconsulta
SELECT 
    f.name,
    ROUND((ni.proteins * 4 / total_energy) * 100, 2) "% de Proteína",
    ROUND((ni.carbohydrates * 4 / total_energy) * 100, 2) "% de Carboidrato",
    ROUND((ni.fats * 9 / total_energy) * 100, 2) "% de Gordura"
FROM foods f
INNER JOIN (SELECT 
		food_id, 
		(proteins * 4 + carbohydrates * 4 + fats * 9) total_energy,
		proteins,
		carbohydrates,
		fats
	FROM nutritional_information) ni
ON f.id = ni.food_id;

-- Usando Common Table Expression
WITH total_energies AS (
	SELECT 
		food_id,
		proteins,
		carbohydrates,
		fats,
		(proteins * 4 + carbohydrates * 4 + fats * 9) total_energy
	FROM nutritional_information
)
SELECT
	f.name,
	ROUND((te.proteins * 4 / te.total_energy) * 100, 2) || '%' "% de Proteína",
    ROUND((te.carbohydrates * 4 / te.total_energy) * 100, 2) || '%' "% de Carboidrato",
    ROUND((te.fats * 9 / te.total_energy) * 100, 2) || '%' "% de Gordura"
FROM total_energies te
INNER JOIN foods f
ON te.food_id = f.id;
