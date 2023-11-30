-- Criar roles
CREATE ROLE dba CREATEDB CREATEROLE BYPASSRLS;
CREATE ROLE desenvolvedor;
CREATE ROLE analista_dados;

-- Adicionar as permissões para as roles
GRANT ALL PRIVILEGES ON DATABASE sql_lesson TO dba;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO dba;

GRANT CONNECT ON DATABASE sql_lesson TO desenvolvedor;
GRANT CREATE ON DATABASE sql_lesson TO desenvolvedor;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO desenvolvedor;

GRANT SELECT ON departments, employees TO analista_dados;

-- Criar usuários
CREATE USER william_dba PASSWORD '123456' IN ROLE dba VALID UNTIL '2024-01-01';

CREATE USER william_dev 
PASSWORD '123456' 
IN ROLE desenvolvedor 
CONNECTION LIMIT 5 
VALID UNTIL '2024-01-01';

CREATE USER william_analista PASSWORD '123456' IN ROLE analista_dados VALID UNTIL '2024-01-01';

-- Revogando permissões
REVOKE DELETE ON ALL TABLES IN SCHEMA public FROM william_dev;
