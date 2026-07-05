# 📚 Minha Biblioteca Pessoal

## 📖 Sobre o Projeto

**Minha Biblioteca Pessoal** é um sistema desenvolvido para auxiliar leitores na organização de seu acervo de livros físicos. A aplicação permite cadastrar livros, acompanhar o status de leitura de cada título e controlar empréstimos realizados a amigos.

O projeto busca solucionar problemas comuns enfrentados por leitores, como esquecer quais livros já foram lidos, quais ainda estão na fila de leitura e quem está com um livro emprestado.

---

## 🎯 Objetivo

Desenvolver uma aplicação que facilite o gerenciamento de uma biblioteca pessoal, proporcionando uma maneira simples e organizada de acompanhar livros e empréstimos.

---

## 👥 Equipe

* Francisca Katielly
* Maria Helloísa
* Marina Louise
* Vitória Cristina

**Disciplina:** Projeto de Desenvolvimento de Software

---

## 👤 Público-alvo

Leitores que desejam organizar seu acervo de livros físicos e controlar empréstimos de maneira prática.

---

## ✨ Funcionalidades

* Cadastro de livros.
* Listagem de todos os livros cadastrados.
* Filtro de livros por:

  * Autor;
  * Gênero;
  * Status de leitura.
* Atualização do status de leitura:

  * Quero Ler;
  * Lendo;
  * Lido.
* Registro de empréstimos para amigos.
* Controle de disponibilidade dos livros.
* Registro de devoluções.
* Identificação de empréstimos em atraso.
* Exclusão de livros que não estejam emprestados.

---

## 📌 Requisitos Funcionais

| ID   | Descrição                                                       |
| ---- | --------------------------------------------------------------- |
| RF01 | Cadastrar livros com título, autor e gênero.                    |
| RF02 | Listar e filtrar livros por status, autor ou gênero.            |
| RF03 | Atualizar o status de leitura de um livro.                      |
| RF04 | Registrar empréstimos para amigos, verificando disponibilidade. |
| RF05 | Registrar devoluções e sinalizar atrasos.                       |
| RF06 | Excluir livros que não estejam emprestados.                     |

---

## ⚙️ Requisitos Não Funcionais

* As buscas e listagens devem ser realizadas em menos de 1 segundo.
* Os dados devem permanecer salvos mesmo após o fechamento da aplicação.
* O sistema deve ser compatível com dispositivos móveis.

---

## 📚 Status de Leitura

Cada livro poderá possuir um dos seguintes status:

* 📖 Quero Ler
* 📘 Lendo
* ✅ Lido

---

## 🤝 Controle de Empréstimos

Ao registrar um empréstimo, o sistema:

* verifica se o livro está disponível;
* registra o nome do amigo;
* define prazo de devolução de 14 dias;
* impede que um livro seja emprestado para mais de uma pessoa ao mesmo tempo.

Ao registrar a devolução:

* o livro volta a ficar disponível;
* caso o prazo seja ultrapassado, o sistema informa que houve atraso.

## 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos na disciplina de Projeto de Desenvolvimento de Software.
