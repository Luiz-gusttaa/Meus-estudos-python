import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AlunoNovo(BaseModel):
    nome: str
    idade: int
    curso_id: int

@app.get("/alunos")
def listar_alunos():
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, idade, curso_id FROM alunos")
    resultado = cursor.fetchall()
    conexao.close()
    return resultado


#@app.delete("/alunos/{nome}")
#def deletar_aluno(nome: str):
#    conexao = sqlite3.connect("escola.db")
#    cursor = conexao.cursor()
#    cursor.execute("DELETE FROM alunos WHERE nome = ?", (nome,))
#    conexao.commit()
#    conexao.close()
#    return {"mensagem": f"Aluno {nome} removido com sucesso"}


#@app.put("/alunos/{aluno_id}")
#def atualizar_aluno(aluno_id: int, aluno: AlunoNovo):
#    conexao = sqlite3.connect("escola.db")
#    cursor = conexao.cursor()
#    cursor.execute(
#        "UPDATE alunos SET nome = ?, idade = ?, curso_id = ? WHERE id = ?",
#        (aluno.nome, aluno.idade, aluno.curso_id, aluno_id)
#   )
#    conexao.commit()
#   conexao.close()
#    return {"mensagem": f"Aluno {aluno_id} atualizado com sucesso"}


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