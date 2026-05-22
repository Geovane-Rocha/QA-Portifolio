# 📚 Estudos de SQL para QA

## O que é um Banco de Dados?
Organiza informações em tabelas com linhas e colunas.

| Termo | Analogia |
|-------|----------|
| Banco de dados | Arquivo Excel |
| Tabela | Aba da planilha |
| Coluna | Cabeçalho |
| Linha/Registro | Uma linha de dados |

## Comandos aprendidos

**CREATE TABLE** — Cria uma tabela
```sql
CREATE TABLE usuarios (
  id INTEGER PRIMARY KEY,
  nome TEXT,
  email TEXT,
  cargo TEXT
);
```

**INSERT** — Insere dados
```sql
INSERT INTO usuarios (id, nome, email, cargo) 
VALUES (1, 'Geovane', 'geovane@email.com', 'QA');
```

**SELECT** — Busca dados
```sql
SELECT * FROM usuarios
SELECT nome, email FROM usuarios
SELECT * FROM usuarios WHERE cargo = 'QA'
```

**UPDATE** — Atualiza dados
```sql
UPDATE usuarios SET email = 'novo@email.com' WHERE id = 1
```

**DELETE** — Remove dados
```sql
DELETE FROM usuarios WHERE id = 1
```

## Uso no dia a dia de QA
- SELECT → validar dados salvos no banco
- UPDATE → preparar massa de dados para teste
- DELETE → limpar dados após os testes
- WHERE → filtrar registros específicos
