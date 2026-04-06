from fastapi import FastAPI, Depends, HTTPException, status
from core.session import get_session

from cadastros.service import AlunoService, ServiceTema


from cadastros.schema import CadastroAluno, AlunoResponse, CadastroTema, ResponseTema


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


@app.post("/tema/cadastrar", response_model=ResponseTema)
def cadastrar_aula(aula: CadastroTema, session=Depends(get_session)):
    try:
        service = ServiceTema(session)
        return service.cadastrar(aula)

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )


@app.get("/tema")
def get_temas(session=Depends(get_session)):
    try:
        service = ServiceTema(session)
        return service.get_aulas()

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )
