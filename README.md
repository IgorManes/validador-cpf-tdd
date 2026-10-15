# Validador de CPF com TDD e Pair Programming

> **Atividade acadêmica.** Este repositório foi criado exclusivamente como
> entrega da Atividade Prática da Aula 13 da disciplina Processo de Engenharia
> de Software (SENAI Goiás, Prof. Luciano Lima). Não é um produto, não deve ser
> usado em produção e não tem relação com nenhuma empresa real. A FlowSoft e os
> chamados #087 e #093 citados aqui são um estudo de caso fictício da disciplina.

## Autor

- Igor ([@IgorManes](https://github.com/IgorManes))

A atividade foi feita em dupla (pair programming). O nome do colega consta no
documento de entrega da disciplina.

## Objetivo da atividade

Construir um validador de CPF aplicando:

- **TDD (Test-Driven Development):** nenhum código de produção é escrito sem
 antes existir um teste falhando (vermelho). Depois, escreve-se o mínimo para
 o teste passar (verde) e, com tudo verde, o código é refatorado.
- **Pair programming:** um integrante digita (piloto) e o outro revisa e orienta
 (copiloto). Os papéis trocam a cada teste verde.

## Como ler o histórico de commits

O histórico registra cada etapa do ciclo de TDD, na ordem em que aconteceu:

- `test(vermelho)`: teste novo escrito e falhando. Esses commits têm testes
 quebrando de propósito, para provar que o teste veio antes do código.
- `feat(verde)`: código mínimo que fez o teste passar.
- `test(passou direto)`: teste que já passou sem alterar o código.
- `wip(regressao)` e `fix(verde)`: momento em que um teste antigo quebrou
 e foi corrigido.
- `refactor`: melhoria na estrutura do código sem mudar o comportamento.

Para ver o histórico completo:

 git log --oneline --reverse

## Como rodar os testes

Requisitos: Python 3 e pytest.

 python -m pip install pytest
 python -m pytest -v

## Comportamentos testados

1. Rejeita texto vazio
2. Rejeita menos de 11 dígitos
3. Rejeita dígitos todos iguais
4. Aceita CPF com pontuação (529.982.247-25)
5. Rejeita letras no meio (bônus)
6. Ignora espaços nas pontas (bônus)
7. Rejeita primeiro dígito verificador errado
8. Rejeita segundo dígito verificador errado
O CPF 529.982.247-25 foi fornecido pelo roteiro da atividade como exemplo de
CPF válido pelo algoritmo.

## Arquivos

- `cpf.py`: código do validador.
- `test_cpf.py`: testes automatizados (pytest).