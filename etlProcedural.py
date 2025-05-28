import requests
from dotenv import load_dotenv, find_dotenv
import os
from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import psycopg2
from datetime import datetime

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_KEY")
api_key = os.getenv("CURRENCY_API_KEY")

"""
problemas com a variável de ambiente. Código para entender onde estava o problema
Solucionado!!

dotenv_path = find_dotenv()
if not dotenv_path:
    print("ATENÇÃO: Arquivo .env não encontrado!")
else:
    print(f"Carregando variáveis de ambiente a partir de: {dotenv_path}")
    load_dotenv(dotenv_path=dotenv_path)

DATABASE_URL = os.getenv("DATABASE_KEY")
print(f"Valor lido para DATABASE_URL após load_dotenv explícito: {DATABASE_URL}")

if not DATABASE_URL:
    print("ERRO: DATABASE_URL não definida. Verifique o arquivo .env e o carregamento.")
    exit() # Ou outra forma de tratamento de erro
"""

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Currency(Base):
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True)
    Real = Column(Float)
    Euro = Column(Float)
    timestamp = Column(DateTime)

Base.metadata.create_all(engine)


def extract():
    url_base = "https://api.freecurrencyapi.com/v1/latest" 
    urlLatest = f"{url_base}?apikey={api_key}"
    responseLatest = requests.get(urlLatest)
    return responseLatest.json()

def transform(dados):
    valor = float(dados['data']['BRL'])
    euro = float(dados['data']['EUR'])
    dado_Tratado = Currency(
        Real = valor,
        Euro = euro,
        timestamp = datetime.now()
    )
    return dado_Tratado

def saveSQL(dados):
    with Session() as session:
        session.add(dados)
        session.commit()
        print("Dados salvos no PostgreSQL")

if __name__ == "__main__":
    dados = extract()
    dado_Tratado = transform(dados)

    saveSQL(dado_Tratado)




