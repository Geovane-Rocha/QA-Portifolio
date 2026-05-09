# Bug Report — BUG-003

## Título
Campo de quantidade no carrinho não permite edição

## Ambiente
- **SO:** Windows
- **Navegador:** Opera GX / Google Chrome
- **Dispositivo:** Computador Desktop

## Pré-condição
Usuário logado com conta `standard_user` 
com ao menos um item adicionado ao carrinho.

## Passos para Reproduzir
1. Acessar https://www.saucedemo.com
2. Fazer login com usuário `standard_user` e senha `secret_sauce`
3. Adicionar um produto ao carrinho
4. Acessar a página do carrinho
5. Tentar editar a quantidade do item na coluna QTY

## Resultado Esperado
O usuário deve conseguir alterar a quantidade de itens 
diretamente no carrinho.

## Resultado Obtido
O campo de quantidade não permite interação ou edição pelo usuário.

## Severidade
🟠 Médio

## Observação
Validar com documentação/requisito se a funcionalidade 
de edição de quantidade no carrinho deveria estar disponível.

## Evidência
> Print a ser adicionado<img width="1299" height="502" alt="QA2" src="https://github.com/user-attachments/assets/6302d21e-fe46-4bcf-accd-018a80397f7e" />
