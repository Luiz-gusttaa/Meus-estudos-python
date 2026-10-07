from pydantic import BaseModel

class AlunoNovo(BaseModel):
    nome: str
    idade: int
    curso_id: int
    id: int