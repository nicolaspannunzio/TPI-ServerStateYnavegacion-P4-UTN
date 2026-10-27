from typing import List
from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from app.core.database import get_session
from app.producto.schema import (
    ProductoCreate, 
    ProductoUpdate, 
    ProductoRead, 
    CategoriaAssign
)
from app.categoria.schema import CategoriaRead
from app.producto import service

router = APIRouter(prefix="/productos", tags=["productos"])

@router.get("/", response_model=List[ProductoRead])
def listar_productos(session: Session = Depends(get_session)):
    return service.get_all_productos(session)

@router.get("/{id}", response_model=ProductoRead)
def obtener_producto(id: int, session: Session = Depends(get_session)):
    return service.get_producto_by_id(id, session)

@router.post("/", response_model=ProductoRead, status_code=status.HTTP_201_CREATED)
def crear_producto(data: ProductoCreate, session: Session = Depends(get_session)):
    return service.create_producto(data, session)

@router.put("/{id}", response_model=ProductoRead)
def editar_producto(id: int, data: ProductoUpdate, session: Session = Depends(get_session)):
    return service.update_producto(id, data, session)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_producto(id: int, session: Session = Depends(get_session)):
    service.delete_producto(id, session)
    return None

# --- Endpoints de relación ProductoCategoria (Unidad 7) ---

@router.post("/{id}/categorias", response_model=ProductoRead, status_code=status.HTTP_201_CREATED)
def asignar_categoria(id: int, body: CategoriaAssign, session: Session = Depends(get_session)):
    return service.assign_categoria_to_producto(id, body.categoria_id, session)

@router.get("/{id}/categorias", response_model=List[CategoriaRead])
def listar_categorias_de_producto(id: int, session: Session = Depends(get_session)):
    return service.get_categorias_of_producto(id, session)

@router.delete("/{id}/categorias/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
def quitar_categoria(id: int, categoria_id: int, session: Session = Depends(get_session)):
    service.remove_categoria_from_producto(id, categoria_id, session)
    return None