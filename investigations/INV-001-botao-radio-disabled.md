# Investigação — INV-001

## Título
Opção "Não" do botão de rádio não responde ao clique

## Site
https://demoqa.com/radio-button

## O que parecia ser um bug
Ao clicar na opção "Não" do botão de rádio, nenhuma ação 
era executada, diferente das opções "Sim" e "Impressionante" 
que funcionavam normalmente.

## O que foi investigado
Utilizei o DevTools do navegador (F12) para inspecionar 
o elemento HTML da opção "Não".

## Resultado da investigação
O elemento contém o atributo `disabled` no código HTML:
```html
<input type="radio" disabled>
```
Isso indica que a opção foi **intencionalmente desabilitada** 
pelos desenvolvedores, não sendo um defeito do sistema.

## Conclusão
❌ Não é um bug — comportamento intencional por design.

## Aprendizado
Antes de reportar um bug, sempre inspecionar o código 
com DevTools para verificar se o comportamento é 
intencional ou um defeito real.

## Evidência
<img width="1102" height="585" alt="QA" src="https://github.com/user-attachments/assets/be1fae3f-0794-4a10-a35f-6d58c2f7f359" />
<img width="1206" height="491" alt="QA2" src="https://github.com/user-attachments/assets/2acf27fb-f4c3-4875-a6d7-e0693ee816e1" />

