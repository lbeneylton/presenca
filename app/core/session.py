from .config import DB_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# o settings é uma instancia das configuraçoes

# Cria o engine do SQLAlchemy para comunicação com o banco
engine = create_engine(DB_settings.sqlalchemy_url, echo=False)

# configura a sessão para o ORM gerenciar a engine e retorna
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Função para entre contínua da sessão
# Cada operação precisara de uma sessão propria


def get_session():
    db = Session()

    try:
        yield db
    finally:
        db.close()
