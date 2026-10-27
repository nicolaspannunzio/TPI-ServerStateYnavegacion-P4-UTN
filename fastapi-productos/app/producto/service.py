from typing import List
from sqlmodel import Session, select, delete
from fastapi import HTTPException, status
from app.producto.model import Producto, ProductoCategoria
from app.producto.schema import ProductoCreate, ProductoUpdate
from app.categoria.model import Categoria

def get_all_productos(session: Session) -> List[Producto]:
    return session.exec(select(Producto)).all()

def get_producto_by_id(producto_id: int, session: Session) -> Producto:
    producto = session.get(Producto, producto_id)
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto con id {producto_id} no encontrado"
        )
    return producto

def create_producto(data: ProductoCreate, session: Session) -> Producto:
    producto = Producto.model_validate(data)
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto

def update_producto(producto_id: int, data: ProductoUpdate, session: Session) -> Producto:
    producto = get_producto_by_id(producto_id, session)
    producto_data = data.model_dump(exclude_unset=True)
    for key, value in producto_data.items():
        setattr(producto, key, value)
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto

def delete_producto(producto_id: int, session: Session) -> None:
    producto = get_producto_by_id(producto_id, session)
    # Limpiamos vínculos de la tabla intermedia
    session.exec(
        delete(ProductoCategoria).where(ProductoCategoria.producto_id == producto_id)
    )
    session.delete(producto)
    session.commit()

# --- Relación ProductoCategoria (Requerimiento Unidad 7) ---

def assign_categoria_to_producto(producto_id: int, categoria_id: int, session: Session) -> Producto:
    producto = get_producto_by_id(producto_id, session)
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Categoría con id {categoria_id} no encontrada"
        )
    
    # Comprobar si ya existe la asociación
    existing = session.exec(
        select(ProductoCategoria).where(
            ProductoCategoria.producto_id == producto_id,
            ProductoCategoria.categoria_id == categoria_id
        )
    ).first()
    
    if not existing:
        vinculo = ProductoCategoria(producto_id=producto_id, categoria_id=categoria_id)
        session.add(vinculo)
        session.commit()
        session.refresh(producto)
        
    return producto

def get_categorias_of_producto(producto_id: int, session: Session) -> List[Categoria]:
    producto = get_producto_by_id(producto_id, session)
    return producto.categorias

def remove_categoria_from_producto(producto_id: int, categoria_id: int, session: Session) -> None:
    get_producto_by_id(producto_id, session)
    vinculo = session.exec(
        select(ProductoCategoria).where(
            ProductoCategoria.producto_id == producto_id,
            ProductoCategoria.categoria_id == categoria_id
        )
    ).first()
    
    if not vinculo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="La relación entre el producto y la categoría no existe"
        )
        
    session.delete(vinculo)
    session.commit()