# 📚 Estudos de Postman e APIs

## O que é uma API?
Interface de comunicação entre sistemas.
Analogia: o garçom que leva o pedido até a cozinha e traz o resultado.

## Métodos HTTP

**GET** — Busca dados (Read)
**POST** — Cria dados (Create)
**PUT** — Atualiza dados (Update)
**DELETE** — Remove dados (Delete)

## Status Codes

| Código | Significado |
|--------|-------------|
| 200 | OK — sucesso |
| 201 | Created — criado com sucesso |
| 400 | Bad Request — dados enviados errados |
| 401 | Unauthorized — sem permissão |
| 404 | Not Found — não encontrado |
| 500 | Internal Server Error — erro no servidor |

## CRUD praticado — JSONPlaceholder

| Método | Endpoint | Status |
|--------|----------|--------|
| GET | /users | 200 OK |
| GET | /users/1 | 200 OK |
| GET | /users/999 | 404 Not Found |
| POST | /users | 201 Created |
| PUT | /users/1 | 200 OK |
| DELETE | /users/1 | 200 OK |

## Aprendizados importantes
- Body só é usado em POST e PUT — DELETE não precisa de Body
- A URL fica na barra superior, não no Body ← erro que cometi e aprendi
- JSON é o formato padrão — o tipo deve estar como JSON no dropdown do raw
- 500 pode indicar erro no formato do Body, não só erro do servidor

## Testes Automáticos com Scripts

O Postman permite escrever validações automáticas na aba **Scripts**.
Isso elimina a necessidade de verificar manualmente cada resposta!

### Validações mais usadas

**Validar Status Code:**
```javascript
pm.test("Status code é 200", function() {
    pm.response.to.have.status(200);
});
```

**Validar se campo existe:**
```javascript
pm.test("Resposta tem nome", function() {
    var json = pm.response.json();
    pm.expect(json.name).to.exist;
});
```

**Validar valor de um campo:**
```javascript
pm.test("ID é igual a 1", function() {
    var json = pm.response.json();
    pm.expect(json.id).to.equal(1);
});
```

## Aprendizados importantes

- A aba Scripts fica em Post-res no Postman
- pm.test() define o nome do teste e a validação
- pm.response.to.have.status() valida o status code
- pm.response.json() converte a resposta para JSON
- pm.expect() faz a validação do valor
- Os resultados aparecem na aba Test Results