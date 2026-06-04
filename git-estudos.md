# 📚 Estudos de Git

## Comandos aprendidos

**git init** — Inicia um novo repositório Git na pasta atual.

**git clone** — Baixa um repositório remoto para o computador.

**git status** — Mostra o que foi alterado e o que está preparado para commit.

**git diff** — Mostra as alterações feitas antes do git add.

**git add .** — Prepara todos os arquivos alterados para o commit.

**git commit -m ""** — Salva as alterações localmente com uma mensagem.

**git push** — Envia os commits para o GitHub.

**git pull** — Baixa as atualizações do GitHub para o computador.

## Fluxo completo do dia a dia

1. git pull
2. Edita os arquivos
3. git diff
4. git add .
5. git commit -m "mensagem"
6. git push

## Aprendizados extras

**Vim** — Editor que abre quando o Git precisa de uma mensagem.
Para sair: Esc → :wq → Enter

**Conflito de merge** — Acontece quando o GitHub tem alterações
que não estão no computador. Solução: git pull antes de git push.

## Comandos Avançados

**git log --oneline** — Mostra histórico de commits de forma resumida.

**git branch** — Lista todas as branches do repositório.

**git branch nome** — Cria uma branch nova.

**git checkout nome** — Entra em uma branch específica.

**git checkout main** — Volta para a branch principal.

**git merge nome** — Une as alterações de uma branch para a branch atual.

**git stash** — Guarda alterações temporariamente sem commitar.

**git stash pop** — Recupera as alterações guardadas no stash.

## Fluxo profissional com branches

1. git pull
2. git branch feature/nome-da-funcionalidade
3. git checkout feature/nome-da-funcionalidade
4. Faz as alterações no VSCode
5. git add .
6. git commit -m "mensagem"
7. git checkout main
8. git merge feature/nome-da-funcionalidade
9. git push

## Aprendizados importantes

- Sempre rodar git pull antes de começar a trabalhar
- Branches isolam o trabalho sem afetar a main
- git stash é útil quando precisa trocar de branch sem commitar
- git log --oneline mostra o histórico de forma limpa
