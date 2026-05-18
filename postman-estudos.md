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