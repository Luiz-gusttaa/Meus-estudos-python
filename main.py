import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AlunoNovo(BaseModel):
    nome: str
    idade: int
    curso_id: int

@app.post("/alunos")
def criar_aluno(aluno: AlunoNovo):
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO alunos (nome, idade, curso_id) VALUES (?, ?, ?)",
        (aluno.nome, aluno.idade, aluno.curso_id)
    )
    conexao.commit()
    conexao.close()
    return {"mensagem": f"Aluno {aluno.nome} criado com sucesso"}
