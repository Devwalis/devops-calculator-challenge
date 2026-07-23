### devops-calculator-challenge
# 🧮 Desafio 1 — Calculadora Básica

## 📖 Sobre o desafio

Este projeto faz parte do **Curso de DevOps** do programa **FAP – Formação Acelerada em Programação**.

O objetivo é desenvolver uma calculadora simples utilizando boas práticas de colaboração com **Git** e **GitHub**, simulando um ambiente de desenvolvimento em equipe.

Durante o desafio, cada integrante é responsável por desenvolver uma funcionalidade em sua própria branch e enviar a implementação por meio de um **Pull Request (PR)**. Após a revisão, as alterações são integradas à branch principal do projeto.

---

## 🎯 Objetivos de aprendizagem

* Trabalhar com Git em equipe.
* Criar e gerenciar branches.
* Realizar commits organizados.
* Abrir Pull Requests.
* Revisar código.
* Resolver conflitos quando necessário.
* Integrar funcionalidades ao projeto principal.

---

## 📋 Funcionalidades

* ➕ Soma
* ➖ Subtração
* ✖️ Multiplicação
* ➗ Divisão
* 📊 Média 

---

## 👥 Divisão das tarefas

| Integrante      | Responsabilidade          | Branch                  |
| --------------- | ------------------------- | ----------------------- |
| Walisson  | Implementar Soma          | `feature/soma`          |
| Patrick  | Implementar Subtração     | `feature/subtracao`     |
| Plínio | Implementar Multiplicação | `feature/multiplicacao` |
| Jader | Implementar Divisão       | `feature/divisao`       |
| Gabriel | Revisão dos Pull Requests | `develop`               |

> A funcionalidade **Média** será implementada como requisito surpresa durante o desafio.

---

## 🌳 Estratégia de Branches

```text
main
│
└── develop
    ├── feature/soma
    ├── feature/subtracao
    ├── feature/multiplicacao
    └── feature/divisao
```

Fluxo de trabalho:

1. Criar uma branch a partir de `develop`.
2. Desenvolver a funcionalidade.
3. Fazer commits descritivos.
4. Enviar a branch para o GitHub.
5. Abrir um Pull Request para `develop`.
6. O revisor analisa o código.
7. Após aprovação, realizar o merge.
8. Ao final do desafio, `develop` é integrada à `main`.

---

## 🚀 Como executar

Clone o repositório:

```bash
git clone <url-do-repositorio>
```

Entre na pasta:

```bash
cd calculadora-basica
```

Execute o projeto conforme a linguagem utilizada pelo grupo.

---

## 📂 Estrutura do projeto

```text
calculadora-basica/
│
├── src/
├── README.md
└── .gitignore
```

---

## 📌 Boas práticas

* Criar commits pequenos e objetivos.
* Utilizar mensagens claras nos commits.
* Sempre atualizar a branch antes de iniciar uma nova tarefa.
* Não realizar commits diretamente na `main`.
* Toda alteração deve passar por Pull Request.

---

## 📚 Tecnologias

* Git
* GitHub
* 

---

## 👨‍💻 Autor

Projeto desenvolvido como atividade prática do **Curso de DevOps** da **FAP – Formação Acelerada em Programação**, com foco na colaboração em equipe utilizando Git e GitHub.
