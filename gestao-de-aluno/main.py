import os

from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException

from database import conectar
from models import AlunoNovo

load_dotenv()

app = FastAPI()

API_KEY = os.getenv("API_KEY")

@app.get("/")
def raiz():
    return {"mensagem": "Minha Primeira API"}

@app.get("/alunos")
def listar_alunos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, idade, curso_id, id FROM alunos")
    resultado = cursor.fetchall()
    conexao.close()
    return resultado

@app.post("/alunos")
def criar_aluno(aluno: AlunoNovo, api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Chave de API inválida")


    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO alunos (nome, idade, curso_id ) VALUES (?, ?, ?)",
        (aluno.nome, aluno.idade, aluno.curso_id,)
    )
    conexao.commit()
    conexao.close()
    return {"mensagem": f"Aluno {aluno.nome} criado com sucesso!"}

@app.put("/alunos/{id}")
def atualizar_aluno(id: int, aluno:AlunoNovo, api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Chave de API inválida")

    conexao  = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE alunos SET nome = ?, idade = ?, curso_id = ? WHERE id = ?",
        (aluno.nome, aluno.idade, aluno.curso_id, id)
    )
    conexao.commit()
    conexao.close()
    return {"Mensagem": f"Aluno {id} atualizado com sucesso!"}

@app.delete("/alunos/{id}")
def deletar_aluno(id: int, api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Chave de API inválida")
    
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM alunos WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()
    return{"mensagem": f"Aluno {id} Removido com sucesso!"}