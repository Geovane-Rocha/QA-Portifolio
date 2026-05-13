# Bug Report — BUG-004

## Título
Botão 'Remove' permanece visível nos produtos após Reset App State

## Ambiente
- **SO:** Windows
- **Navegador:** Opera GX / Google Chrome
- **Dispositivo:** Computador Desktop

## Pré-condição
Usuário deve estar logado em https://www.saucedemo.com
e ter produtos adicionados ao carrinho.

## Passos para Reproduzir
1. Acessar https://www.saucedemo.com
2. Fazer login com usuário `standard_user` e senha `secret_sauce`
3. Adicionar itens no carrinho
4. Clicar nos três traços do canto superior esquerdo
5. Clicar em "Reset App State"
6. Voltar para a página de produtos e observar os botões

## Resultado Esperado
Após o reset, o botão "Remove" deve desaparecer dos produtos,
sendo substituído pelo botão "Add to cart".

## Resultado Obtido
O "Reset App State" ao ser clicado remove os produtos do
carrinho mas o botão "Remove" continua visível nos produtos.

## Severidade
🟡 Baixa

## Prioridade
🟡 Baixa

## Impacto
Baixo impacto funcional, porém pode confundir o usuário
ao perceber que os produtos foram removidos do carrinho
mas o botão "Remove" ainda aparece nos produtos.

## Evidência


![evidencia-bug-004](https://github.com/user-attachments/assets/49a1b54b-3acf-478e-beda-7aa9567a1919)

