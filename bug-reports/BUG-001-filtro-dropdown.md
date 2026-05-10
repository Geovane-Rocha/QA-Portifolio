# BUG-001 — Seta do filtro de ordenação não abre o dropdown ao ser clicada

## Ambiente
- **SO:** Windows
- **Navegador:** Opera GX / Google Chrome
- **Dispositivo:** Computador Desktop

## Pré-condição
Usuário deve estar logado com a conta `standard_user` e estar na página de produtos.

## Passos para Reproduzir
1. Acessar https://www.saucedemo.com
2. Fazer login com usuário `standard_user` e senha `secret_sauce`
3. Na página de produtos, localizar o campo de filtro no canto superior direito
4. Clicar especificamente na **seta (ícone)** do dropdown, não no texto

## Resultado Esperado
Uma ação é executada ao clicar na seta. O dropdown abre normalmente.

## Resultado Obtido
Nenhuma ação é executada ao clicar na seta. O dropdown só abre quando o clique é feito
diretamente no texto 'Name (A to Z)', ignorando a área clicável do ícone.

## Severidade
🟡 Baixo

## Evidência
> Print a ser adicionado
