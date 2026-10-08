import os

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Header, HTTPException

from database import conectar
from models import AlunoNovo

load_dotenv()

app = FastAPI()

API_KEY = os.getenv("API_KEY")

def verificar_chave(api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Chave de API Inválida")

@app.get("/")
def raiz():
    return {"mensagem": "Minha Primeira API"}

@app.get("/alunos")
def listar_alunos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT alunos.id, alunos.nome, alunos.idade, cursos.nome AS curso
    FROM  alunos
    LEFT JOIN cursos ON alunos.curso_id = cursos.id    
"""
    )
    resultado = cursor.fetchall()
    alunos1: list[dict[str, int | str | None]]=[]
    for i in resultado:
            aluno = {
            "id":i[0], "nome": i[1], "idade": i[2], "curso": i[3]
            }
            alunos1.append(aluno)

    conexao.close()
    return alunos1


@app.post("/alunos", dependencies=[Depends(verificar_chave)])
def criar_aluno(aluno: AlunoNovo):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO alunos (nome, idade, curso_id ) VALUES (?, ?, ?)",
        (aluno.nome, aluno.idade, aluno.curso_id,)
    )
    conexao.commit()
    conexao.close()
    return {"mensagem": f"Aluno {aluno.nome} criado com sucesso!"}

@app.put("/alunos/{id}", dependencies=[Depends(verificar_chave)])
def atualizar_aluno(id: int, aluno:AlunoNovo):
    conexao  = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE alunos SET nome = ?, idade = ?, curso_id = ? WHERE id = ?",
        (aluno.nome, aluno.idade, aluno.curso_id, id)
    )
    conexao.commit()

    if cursor.rowcount == 0:    
        conexao.close()
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    conexao.close()
    return {"Mensagem": f"Aluno {id} atualizado com sucesso!"}

@app.delete("/alunos/{id}", dependencies=[Depends(verificar_chave)])
def deletar_aluno(id: int,):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM alunos WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()
    return{"mensagem": f"Aluno {id} Removido com sucesso!"}