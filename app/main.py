from fastapi import FastAPI, Depends, HTTPException, status
from core.session import get_session

from cadastros.service import AlunoService, AulaService


from cadastros.schema import CadastroAluno, AlunoResponse, CadastroAula, AulaResponse


app = FastAPI()


@app.get("/")
def home():
    return {"sucesso": True}


@app.post("/aluno/cadastrar", response_model=AlunoResponse)
def cadastrar_aluno(aluno: CadastroAluno, session=Depends(get_session)):
    try:
        service = AlunoService(session)
        return service.cadastrar(aluno)

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )


@app.post("/aula/cadastrar", response_model=AulaResponse)
def cadastrar_aula(aula: CadastroAula, session=Depends(get_session)):
    try:
        service = AulaService(session)
        return service.cadastrar(aula)

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )


@app.get("/aula")
def get_aulas(session=Depends(get_session)):
    try:
        service = AulaService(session)
        return service.get_aulas()

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )
