-- Iniciando a transação
BEGIN;

DELETE FROM employees;

INSERT INTO employees (id, name, age, salary, department_id) VALUES (1, 'Arlindo', 42, 3500, 1);
-- Criando um ponto de retorno na transação
SAVEPOINT novo_cliente;

DELETE FROM employees;

-- Voltando para o savepoint
ROLLBACK TO novo_cliente;

-- Removendo o savepoint
RELEASE SAVEPOINT novo_cliente;

-- Voltando para o estado inicial da transação
ROLLBACK;

UPDATE employees SET name = 'Arlindo' WHERE id = 1;

-- Salvando as alterações da transação
COMMIT;

SELECT * FROM employees;

