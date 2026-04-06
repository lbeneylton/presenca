from db.models import Aluno, Aula

from .schema import CadastroAluno, CadastroAula

from sqlalchemy.orm import Session

from sqlalchemy import select


class AlunoService:
    def __init__(self, session: Session) -> None:
        self.session = session

    def cadastrar(self, aluno: CadastroAluno):
        novo_aluno = Aluno(
            nome=aluno.nome,
            contato=aluno.contato,
            data_matricula=aluno.data_matricula,
            tipo=aluno.tipo,
            status="Ativo",
            turno=aluno.turno,
            outro_curso=aluno.outro_curso
        )
        self.session.add(novo_aluno)
        self.session.commit()
        self.session.refresh(novo_aluno)

        return novo_aluno


class AulaService:
    def __init__(self, session: Session) -> None:
        self.session = session

    def cadastrar(self, aula: CadastroAula):
        nova_aula = Aula(
            nome=aula.nome
        )
        self.session.add(nova_aula)
        self.session.commit()
        self.session.refresh(nova_aula)

        return nova_aula

    def get_aulas(self):
        stmt = select(Aula)
        return self.session.scalars(stmt).all()
