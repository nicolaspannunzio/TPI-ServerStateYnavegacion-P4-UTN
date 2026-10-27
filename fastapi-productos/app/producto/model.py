from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import ARRAY
from app.categoria.model import Categoria

class ProductoCategoria(SQLModel, table=True):
    __tablename__ = "producto_categoria"

    producto_id: Optional[int] = Field(
        default=None, foreign_key="productos.id", primary_key=True
    )
    categoria_id: Optional[int] = Field(
        default=None, foreign_key="categorias.id", primary_key=True
    )

class ProductoBase(SQLModel):
    nombre: str = Field(index=True)
    descripcion: str
    precio_base: float = Field(ge=0)
    imagenes_url: List[str] = Field(
        default_factory=list,
        sa_column=Column(ARRAY(String))
    )
    disponible: bool = True

class Producto(ProductoBase, table=True):
    __tablename__ = "productos"

    id: Optional[int] = Field(default=None, primary_key=True)
    
    # Aquí link_model recibe directamente la clase ProductoCategoria
    categorias: List[Categoria] = Relationship(
        link_model=ProductoCategoria
    )