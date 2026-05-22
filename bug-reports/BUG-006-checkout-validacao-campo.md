# Bug Report - BUG-006

## Título
Checkout: campo de informações aceita números onde
deveria ser caracteres

## Ambiente
- **SO:** Windows
- **Navegador:** Opera GX / Google Chrome
-**Dispositivo:** Computador Desktop

## Pré-conndição
Usuário deve estar na página 
https://www.saucedemo.com/checkout-step-one.html

## Passos para Reproduzir
1. Acessar https://www.saucedemo.com
2. Fazer login com usuário 'standard_user' e senha 'secret_sauce'
3. Adicionar um produto ao carrinho
4. Clicar no ícone do carrinho
5. Clicar em "Checkout"
6. No campo "First Name" digitar número: '12345'
7. No campo "Last Name" digitar número: '12345'
8. No campo "Zip Code" digitar letras: 'abcde'
9. Clicar em "Continue"

## Resultado Esperado
Ao digitar números no campo nome e sobrenome e caracteres no campo código postal deveria aparecer mensagem  de inválido.

## Resultado Obtido
O sistema aceita os dados inválidos efinaliza a campra
perfeitamente sem nenhumavalidação.

## Severidade
🔴 Alta

## Prioridade
🔴 Alta

## Impcato
Impacta tanto o usuário quanto o recptor - um dado errado
pode dificultar localizar as informações do usuário e prejudicar a loja.

## Evidencia
<img width="1170" height="527" alt="sauce" src="https://github.com/user-attachments/assets/2eade99d-bca5-43d4-82d8-b108c1eb032f" />
