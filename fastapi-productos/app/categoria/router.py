from typing import List
from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from app.core.database import get_session
from app.categoria.schema import CategoriaCreate, CategoriaUpdate, CategoriaRead
from app.categoria import service

router = APIRouter(prefix="/categorias", tags=["categorias"])

@router.get("/", response_model=List[CategoriaRead])
def listar_categorias(session: Session = Depends(get_session)):
    return service.get_all_categorias(session)

@router.get("/{id}", response_model=CategoriaRead)
def obtener_categoria(id: int, session: Session = Depends(get_session)):
    return service.get_categoria_by_id(id, session)

@router.post("/", response_model=CategoriaRead, status_code=status.HTTP_201_CREATED)
def crear_categoria(data: CategoriaCreate, session: Session = Depends(get_session)):
    return service.create_categoria(data, session)

@router.put("/{id}", response_model=CategoriaRead)
def editar_categoria(id: int, data: CategoriaUpdate, session: Session = Depends(get_session)):
    return service.update_categoria(id, data, session)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_categoria(id: int, session: Session = Depends(get_session)):
    service.delete_categoria(id, session)
    return None