# Enhancement — ENH-001

## Título
Campo numérico não exibe mensagem orientando o usuário
a digitar apenas números

## Ambiente
- **SO:** Windows
- **Navegador:** Opera GX / Google Chrome
- **Dispositivo:** Computador Desktop

## Pré-condição
Usuário deve estar na página inicial do the-internet.herokuapp.com

## Passos para Reproduzir
1. Acessar https://the-internet.herokuapp.com
2. Clicar em **Inputs** no menu
3. Digitar caracteres ou caracteres especiais `*&%$?^~[]{}`

## Resultado Esperado
Ao digitar caracteres deve aparecer mensagem de alerta
"apenas números".

## Resultado Obtido
Ao digitar caracteres não aparece nenhuma mensagem de aviso.

## Severidade
🔵 Enhancement

## Prioridade
🟡 Baixa

## Impacto
Usuário pode ficar confuso ao não receber feedback sobre
o tipo de dado aceito no campo, mesmo com o label
"Number" visível acima.

## Evidência
> Print a ser adicionado