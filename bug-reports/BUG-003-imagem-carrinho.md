# Bug Report — BUG-003

## Título
Imagem do produto não aparece na página do carrinho

## Ambiente
- **SO:** Windows
- **Navegador:** Opera GX / Google Chrome
- **Dispositivo:** Computador Desktop

## Pré-condição
Usuário deve estar logado com a conta `standard_user` 
e estar na página do carrinho com produtos adicionados.

## Passos para Reproduzir
1. Acessar https://www.saucedemo.com
2. Fazer login com usuário `standard_user` e senha `secret_sauce`
3. Na página de produtos, clicar em "Add to cart" em qualquer produto
4. Clicar no ícone do carrinho no canto superior direito
5. Observar os itens listados no carrinho

## Resultado Esperado
As imagens de cada produto devem aparecer no carrinho 
para que o usuário confirme visualmente o item correto.

## Resultado Obtido
Nenhuma imagem aparece quando o usuário acessa o carrinho. 
A imagem só é exibida ao clicar no nome do produto.

## Severidade
🟠 Médio

## Evidência
<img width="1308" height="501" alt="QA3" src="https://github.com/user-attachments/assets/df84b551-32a0-4a0e-b6d0-1e40f767f570" />
