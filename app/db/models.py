from .base import Base

from sqlalchemy import Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import date


class Aluno(Base):
    __tablename__ = 'Aluno'

    # Dados do Aluno
    id_aluno: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    contato: Mapped[str] = mapped_column(String(20))

    # Dados sobre o aluno
    data_matricula: Mapped[date] = mapped_column(Date, nullable=False)
    tipo: Mapped[str] = mapped_column(
        String(1), nullable=False, default='A')  # ADULTO ou KIDS

    status: Mapped[str] = mapped_column(String(10))
    turno: Mapped[str] = mapped_column(
        String(1), nullable=False)  # MANHA  OU TARDE

    certificado: Mapped[bool] = mapped_column(Boolean, default=False)
    outro_curso: Mapped[bool] = mapped_column(Boolean, default=False)

    # Relationship
    presencas = relationship("Presenca", back_populates="Aluno")


class Aula(Base):
    __tablename__ = "Aula"

    id_aula: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)

    # Relationship
    presencas = relationship("Presenca", back_populates="Aula")


class Presenca(Base):
    __tablename__ = "Presenca"

    id_aluno: Mapped[int] = mapped_column(
        Integer, ForeignKey("Aluno.id_aluno"), primary_key=True
    )

    id_aula: Mapped[int] = mapped_column(
        Integer, ForeignKey("Aula.id_aula"), primary_key=True
    )

    data: Mapped[date] = mapped_column(Date, nullable=False, primary_key=True)

    # Relacionamentos
    Aluno = relationship("Aluno", back_populates="presencas")
    Aula = relationship("Aula", back_populates="presencas")
