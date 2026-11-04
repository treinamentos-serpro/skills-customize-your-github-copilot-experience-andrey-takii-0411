# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST com FastAPI para gerenciar uma coleção de livros. Você praticará rotas HTTP, validação de dados com Pydantic e respostas com códigos de status apropriados.

## 📝 Tasks

### 🛠️ Configure a aplicação e crie uma rota de saúde

#### Descrição
Prepare o ambiente, execute o servidor FastAPI e implemente uma rota simples para confirmar que a API está disponível.

#### Requisitos
O programa concluído deve:

- Instalar FastAPI e Uvicorn com `pip install fastapi uvicorn`.
- Iniciar o servidor executando `python starter-code.py`.
- Responder a uma requisição `GET /health` com um objeto JSON que indique que a API está funcionando.
- Exibir a documentação interativa da API em `/docs`.


### 🛠️ Criar e consultar livros

#### Descrição
Implemente operações para adicionar livros à coleção em memória e consultar todos os livros ou um livro específico pelo ID. Use o modelo Pydantic fornecido para validar os dados recebidos.

#### Requisitos
O programa concluído deve:

- Aceitar `title`, `author` e `year` em `POST /books` e retornar o livro criado com um ID e status `201`.
- Rejeitar dados inválidos, como título ou autor vazio e ano negativo, com o erro de validação do FastAPI.
- Retornar a coleção completa em `GET /books`.
- Retornar um livro em `GET /books/{book_id}` ou status `404` quando o ID não existir.


### 🛠️ Atualizar e remover livros

#### Descrição
Complete as operações de atualização e remoção, mantendo a coleção em memória consistente.

#### Requisitos
O programa concluído deve:

- Atualizar os dados de um livro existente em `PUT /books/{book_id}`.
- Retornar status `404` ao tentar atualizar ou remover um livro inexistente.
- Remover um livro existente em `DELETE /books/{book_id}` e retornar status `204` sem conteúdo.
- Permitir testar todas as operações pela documentação interativa em `/docs`.