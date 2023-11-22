CREATE TABLE IF NOT EXISTS public.criminosos (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(256) NOT NULL,
	cpf VARCHAR(11) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS public.vitimas (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(256) NOT NULL,
	cpf VARCHAR(11) NOT NULL UNIQUE,
	telefone VARCHAR(20) NOT NULL,
	crime_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.crimes (
	id SERIAL PRIMARY KEY,
	descricao VARCHAR(256) NOT NULL,
	data TIMESTAMP NOT NULL,
	data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.armas (
	id SERIAL PRIMARY KEY,
	calibre VARCHAR(20) NOT NULL,
	modelo VARCHAR(256) NOT NULL,
	fabricante VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.locais (
	id SERIAL PRIMARY KEY,
	logradouro VARCHAR(256) NOT NULL,
	cidade VARCHAR(256) NOT NULL,
	bairro VARCHAR(256) NOT NULL,
	estado VARCHAR(256) NOT NULL,
	crime_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.armas_crimes (
	arma_id INT,
	crime_id INT,
	PRIMARY KEY (arma_id, crime_id)
);

CREATE TABLE IF NOT EXISTS public.vitimas_crimes (
	vitima_id INT,
	crime_id INT,
	PRIMARY KEY (vitima_id, crime_id)
);

CREATE TABLE IF NOT EXISTS public.crimes_criminosos (
	criminoso_id INT,
	crime_id INT,
	PRIMARY KEY (criminoso_id, crime_id)
);

-- Adicionando as chaves-estrangeiras
ALTER TABLE IF EXISTS public.locais
ADD FOREIGN KEY (crime_id)
REFERENCES public.crimes (id)
ON UPDATE CASCADE
ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.vitimas
ADD FOREIGN KEY (crime_id)
REFERENCES public.crimes (id)
ON UPDATE CASCADE
ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.armas_crimes
ADD FOREIGN KEY (arma_id)
REFERENCES public.armas (id)
ON UPDATE CASCADE
ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.armas_crimes
ADD FOREIGN KEY (crime_id)
REFERENCES public.crimes (id)
ON UPDATE CASCADE
ON DELETE RESTRICT;

ALTER TABLE IF EXISTS public.crimes_criminosos
ADD FOREIGN KEY (crime_id)
REFERENCES public.crimes (id)
ON UPDATE CASCADE
ON DELETE SET NULL;

ALTER TABLE IF EXISTS public.crimes_criminosos
ADD FOREIGN KEY (criminoso_id)
REFERENCES public.criminosos (id);

ALTER TABLE IF EXISTS public.vitimas_crimes
ADD FOREIGN KEY (crime_id)
REFERENCES public.crimes (id);

ALTER TABLE IF EXISTS public.vitimas_crimes
ADD FOREIGN KEY (vitima_id)
REFERENCES public.vitimas (id);

-- Renomeando
-- ALTER TABLE locais RENAME TO localizacoes;

-- Remoção de tabelas
-- DROP TABLE localizacoes;

-- Remoção de base de dados
-- DROP DATABASE delegacia;

-- Truncar tabela
-- TRUNCATE criminosos RESTART IDENTITY CASCADE;
