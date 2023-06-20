from sqlalchemy.sql.traversals import anon_map

from . import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from .database import get_db

router = APIRouter()


# [...] get all records
@router.get('/')
def get_anotacoes(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    anotacoes = db.query(models.Anotacao).filter(
        models.Anotacao.titulo.contains(search)).limit(limit).offset(skip).all()

    return {'status': 'success', 'results': len(anotacoes), 'anotacoes': anotacoes}


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_anotacao(payload: schemas.AnotacaoBaseSchema, db: Session = Depends(get_db)):
    new_anotacao = models.anotacao(**payload.dict())
    db.add(new_anotacao)
    db.commit()
    db.refresh(new_anotacao)

    return {"status": "success", "anotacao": new_anotacao}


@router.patch('/{anotacao_id}')
def update_anotacao(anotacao_id: str, payload: schemas.AnotacaoBaseSchema, db: Session = Depends(get_db)):
    anotacao_query = db.query(models.Anotacao).filter(models.Anotacao.id == anotacao_id)
    db_anotacao = anotacao_query.first()

    if not db_anotacao:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Nenhuma anotação com este ID: {anotacao_id} foi encontrada')

    update_data = payload.dict(exclude_unset=True)
    anotacao_query.filter(models.Anotacao.id == anotacao_id).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(db_anotacao)

    return {"status": "success", "anotacao": db_anotacao}


@router.get('/{anotacao_id}')
def get_anotacao(payload: schemas.AnotacaoBaseSchema, db: Session = Depends(get_db)):
    new_anotacao = models.Anotacao(**payload.dict())
    db.add(new_anotacao)
    db.commit()
    db.refresh(new_anotacao)

    return {"status": "success", "anotacao": new_anotacao}


@router.patch('/{anotacao_id}')
def update_note(anotacao_id: str, db: Session = Depends(get_db)):
    anotacao = db.query(models.Anotacao).filter(models.Anotacao.id == anotacao_id).first()

    if not anotacao:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Nenhuma anotação com este ID: {anotacao_id} foi encontrada")

    return {"status": "success", "anotacao": anotacao}


@router.delete('/{anotacao_id}')
def delete_anotacao(anotacao_id: str, db: Session = Depends(get_db)):
    anotacao_query = db.query(models.Anotacao).filter(models.Anotacao.id == anotacao_id)
    anotacao = anotacao_query.first()

    if not anotacao:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Nenhuma anotação com este ID: {anotacao_id} foi encontrada')

    anotacao_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
