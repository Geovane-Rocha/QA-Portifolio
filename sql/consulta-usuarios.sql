-- Projeto de estudos SQL para Quality Assurance
-- Consultas para validação de dados
SELECT * FROM usuarios;

-- Teste 2: consultar um usuário específico pelo nome
SELECT * FROM usuarios
WHERE nome = 'Carlos';

-- Teste 3: consultar usuários com idade maior que 30
SELECT * FROM usuarios
WHERE idade > 30;

-- Teste 4: consultar usuários entre 25 e 40 anos
SELECT * FROM usuarios
WHERE idade >= 25 AND idade  <= 40;

-- Teste 5: consultar os usuários Larissa OU Carlos
SELECT * FROM usuarios
WHERE nome = 'Larissa' OR nome = 'Carlos';

-- Teste 6: consultar usuários com menos de 30 anos OU mais de 40 anos
SELECT * FROM usuarios
WHERE idade < 30 OR idade > 40;

-- Teste 7: consultar usuários cujo nome começa com a letra G
SELECT * FROM usuarios
WHERE nome LIKE 'G%';

-- Teste 8: consultar usuários cujo nome contém a letra "a" e ordenar do mais velho para o mais novo
SELECT * FROM usuarios
WHERE nome LIKE '%a%'
ORDER BY idade DESC;

-- Teste 9: consultar nome e idade dos usuários com 30 anos ou mais,
-- ordenando do mais velho para o mais novo
SELECT nome, idade FROM usuarios
WHERE idade >= 30
ORDER BY idade DESC;

-- Teste 10: consultar nome e email dos usuários com menos de 30 anos
-- ordenando os nomes em ordem crescente

SELECT nome, email FROM usuarios
WHERE idade < 30
ORDER BY nome ASC;


-- Teste 11: consultar usuários específicos utilizando IN

SELECT * FROM usuarios
WHERE id IN (1, 3, 4);


-- Teste 12: consultar nome e idade dos usuários entre 20 e 35 anos

SELECT nome, idade FROM usuarios
WHERE idade BETWEEN 20 AND 35;