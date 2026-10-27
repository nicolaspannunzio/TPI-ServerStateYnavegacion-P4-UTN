from typing import Optional, List
from sqlmodel import SQLModel
from app.categoria.schema import CategoriaRead

class ProductoCreate(SQLModel):
    nombre: str
    descripcion: str
    precio_base: float
    imagenes_url: List[str] = []
    disponible: bool = True

class ProductoUpdate(SQLModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio_base: Optional[float] = None
    imagenes_url: Optional[List[str]] = None
    disponible: Optional[bool] = None

class ProductoRead(SQLModel):
    id: int
    nombre: str
    descripcion: str
    precio_base: float
    imagenes_url: List[str]
    disponible: bool
    categorias: List[CategoriaRead] = []

class CategoriaAssign(SQLModel):
    categoria_id: int