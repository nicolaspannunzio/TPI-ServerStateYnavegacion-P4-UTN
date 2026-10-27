from typing import List
from sqlmodel import Session, select, delete
from fastapi import HTTPException, status
from app.categoria.model import Categoria
from app.categoria.schema import CategoriaCreate, CategoriaUpdate
from app.producto.model import ProductoCategoria

def get_all_categorias(session: Session) -> List[Categoria]:
    return session.exec(select(Categoria)).all()

def get_categoria_by_id(categoria_id: int, session: Session) -> Categoria:
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoría con id {categoria_id} no encontrada"
        )
    return categoria

def create_categoria(data: CategoriaCreate, session: Session) -> Categoria:
    categoria = Categoria.model_validate(data)
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria

def update_categoria(categoria_id: int, data: CategoriaUpdate, session: Session) -> Categoria:
    categoria = get_categoria_by_id(categoria_id, session)
    categoria_data = data.model_dump(exclude_unset=True)
    for key, value in categoria_data.items():
        setattr(categoria, key, value)
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria

def delete_categoria(categoria_id: int, session: Session) -> None:
    categoria = get_categoria_by_id(categoria_id, session)
    # Limpiamos relaciones en la tabla intermedia antes de eliminar
    session.exec(
        delete(ProductoCategoria).where(ProductoCategoria.categoria_id == categoria_id)
    )
    session.delete(categoria)
    session.commit()