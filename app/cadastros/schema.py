from pydantic import BaseModel
from typing import Optional

from datetime import date


class CadastroAluno(BaseModel):
    nome: str
    contato: str
    data_matricula: date

    tipo: Optional[str] = 'A'
    turno: Optional[str] = 'M'

    outro_curso: bool = False


class AlunoResponse(BaseModel):
    id_aluno: int
    nome: str
    status: str


class CadastroTema(BaseModel):
    nome: str


class ResponseTema(BaseModel):
    id_aula: int
    nome: str
