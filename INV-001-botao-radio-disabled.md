# Investigações - INV-001

## Título
Opção "Não" do botão de rádio não responde ao clique

## Site
https://demoqa.com/radio-button

## O que parecia ser um bug 
Ao clicar na opção "Não" do botão de rádio, nenhuma ação
era executada, diferente da opções "Sim" e "Impressionante"
 que funciona normalmente.

## O que foi investigado
Utilizei o DevTools do navegador (F12) para inspecionar
o elemento HTML da opção "Não".

## Resultado da investigação
O elemento contém o atributo 'disabled' no código HTML:
<input type="radio" disabled>
