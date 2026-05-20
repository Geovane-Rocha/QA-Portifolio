# Investigação — INV-002

## Título
Typo aleatório aparece na página /typos a cada recarregamento

## Site
https://the-internet.herokuapp.com/typos

## O que parecia ser um bug
Ao recarregar a página, a cada 2/3 vezes aparece um erro
de digitação no segundo parágrafo:
"...outras vezes você vai, não."

## O que foi investigado
Leitura atenta do próprio conteúdo da página que explica
o comportamento.

## Resultado da investigação
O próprio site informa:
"Este exemplo demonstra um erro de digitação que está sendo
introduzido. Ele faz aleatoriamente em cada carregamento
de página."

O typo é **intencional e aleatório** — foi criado para
treinar QAs a identificar erros de digitação em textos.

## Conclusão
❌ Não é um bug — comportamento intencional por design.

## Aprendizado
Antes de reportar um bug, sempre ler atentamente o
contexto da página — às vezes o próprio sistema explica
o comportamento.

## Evidência
<img width="1127" height="415" alt="ggt" src="https://github.com/user-attachments/assets/65c5f0b8-32f3-40fd-8348-5139beaddd06" />
9adcebc544dec5d98c99f138eec2d17e61bf7473
