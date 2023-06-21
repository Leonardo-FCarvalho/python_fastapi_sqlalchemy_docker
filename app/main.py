# from fastapi import FastAPI, APIRouter, status
from app import models, anotacao
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(anotacao.router, tags=['Anotações'], prefix='/api/anotacoes')


# @router.get('/')
# def get_anotacoes():
#     return "Retorna uma lista de Anotações"


# @router.post('/', status_code=status.HTTP_201_CREATED)
# def create_anotacao():
#     return "Cria uma Anotação"


# @router.patch('/{anotacao_id}')
# def update_anotacao(anotacao_id: str):
#     return f"Altera a Anotação com ID {anotacao_id}"


# @router.get('/{pessoa_fisica_id}')
# def get_anotacao(anotacao_id: str):
#     return f"Obtem a Anotação com ID {anotacao_id}"


# @router.delete('/{anotacao_id}')
# def delete_anotacao(anotacao_id: str):
#     return f"Exclui a Anotação com ID {anotacao_id}"


# app.include_router(router, tags=['Anotações'], prefix='/api/anotacaos')


@app.get("/api/home")
def root():
    return {"message": "Aplicação Python com Framework FastAPI, ORM SQLAlchemy e Banco de Dados PostegreSQL"}
