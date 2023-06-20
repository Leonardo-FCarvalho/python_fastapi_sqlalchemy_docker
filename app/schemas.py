from datetime import datetime
from typing import List
from pydantic import BaseModel


class AnotacaoBaseSchema(BaseModel):
    id: str | None = None
    tituto: str
    descricao: str
    data_criacao: datetime | None = None
    data_alteracao: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListAnotacaoResponse(BaseModel):
    status: str
    results: int
    notes: List[AnotacaoBaseSchema]
