# 📘 Assignment: Persisting FastAPI Data with SQLite

## 🎯 Objective

Evolua a API de livros para armazenar os dados em SQLite em vez de mantê-los apenas na memória. Você praticará criação de tabelas, consultas SQL parametrizadas e persistência de operações CRUD.

## 📝 Tasks

### 🛠️ Create the SQLite database schema

#### Descrição
Implemente a inicialização do banco de dados para que a API crie a tabela de livros automaticamente ao iniciar.

#### Requisitos
O programa concluído deve:

- Criar o arquivo `books.db` no diretório da assignment.
- Criar uma tabela `books` com ID autoincremental e colunas para título, autor e ano.
- Usar `CREATE TABLE IF NOT EXISTS` para que iniciar a API novamente não apague os dados existentes.
- Ser executável com `python starter-code.py` após instalar FastAPI e Uvicorn.


### 🛠️ Persist books with SQLite queries

#### Descrição
Substitua o armazenamento em memória por consultas ao SQLite para criar livros e consultar a coleção ou um livro pelo ID.

#### Requisitos
O programa concluído deve:

- Inserir livros em `POST /books` e retornar o registro criado com status `201`.
- Retornar todos os registros em `GET /books` e um registro específico em `GET /books/{book_id}`.
- Retornar status `404` quando o ID solicitado não existir.
- Usar consultas parametrizadas com placeholders `?`, sem interpolar valores diretamente no SQL.


### 🛠️ Update and delete persistent books

#### Descrição
Implemente atualização e remoção de livros no banco e confirme que as alterações continuam disponíveis após reiniciar o servidor.

#### Requisitos
O programa concluído deve:

- Atualizar um livro existente em `PUT /books/{book_id}` e retornar o registro atualizado.
- Remover um livro existente em `DELETE /books/{book_id}` e retornar status `204` sem conteúdo.
- Retornar status `404` para atualização ou remoção de um ID inexistente.
- Fechar as conexões com o banco e confirmar que os registros sobrevivem a uma reinicialização da API.