from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE


class Anotacao(Base):
    __tablename__ = 'anotacao'
    
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    data_criacao = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    data_alteracao = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())
    ativa = Column(Boolean, nullable=False, default=True)
