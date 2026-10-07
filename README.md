# API de Gestão de Alunos

API REST simples para gerenciar alunos e cursos, desenvolvida com FastAPI e SQLite como projeto de estudos em backend com Python.

## Funcionalidades

- Listar todos os alunos cadastrados
- Buscar aluno por nome
- Cadastrar novo aluno
- Atualizar dados de um aluno existente
- Remover aluno
- Relacionamento entre alunos e cursos (via banco de dados)

## Tecnologias

- Python
- FastAPI
- SQLite
- Uvicorn

## Como rodar

1. Clone o repositório
```bash
git clone https://github.com/Luiz-gusttaa/Meus-estudos-python.git
cd Meus-estudos-python
```

2. Instale as dependências
```bash
pip install fastapi uvicorn
```

3. Inicie o servidor
```bash
uvicorn main:app --reload
```

4. Acesse a documentação interativa
```
http://127.0.0.1:8000/docs
```

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | `/alunos` | Lista todos os alunos |
| GET | `/alunos/{nome}` | Busca aluno por nome |
| POST | `/alunos` | Cadastra um novo aluno |
| PUT | `/alunos/{aluno_id}` | Atualiza um aluno existente |
| DELETE | `/alunos/{nome}` | Remove um aluno |

## Sobre o projeto

Este projeto foi construído como parte dos meus estudos de programação, cobrindo desde lógica básica até backend com API REST e banco de dados relacional. Durante o desenvolvimento, pratiquei:

- Lógica de programação e estruturas de dados em Python
- Programação orientada a objetos (classes e herança)
- SQL e modelagem de banco de dados relacional
- Construção de APIs REST com FastAPI
- Controle de versão com Git/GitHub
