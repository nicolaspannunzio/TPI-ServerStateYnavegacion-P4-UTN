from typing import Optional, List
from sqlmodel import SQLModel, Field
from app.categoria.schema import CategoriaRead

class ProductoCreate(SQLModel):
    nombre: str = Field(min_length=1, max_length=150)
    descripcion: str = Field(default="", max_length=1000)
    precio_base: float = Field(ge=0)
    imagenes_url: List[str] = Field(default_factory=list)
    disponible: bool = True

class ProductoUpdate(SQLModel):
    nombre: Optional[str] = Field(default=None, min_length=1, max_length=150)
    descripcion: Optional[str] = Field(default=None, max_length=1000)
    precio_base: Optional[float] = Field(default=None, ge=0)
    imagenes_url: Optional[List[str]] = None
    disponible: Optional[bool] = None

class ProductoRead(SQLModel):
    id: int
    nombre: str
    descripcion: str
    precio_base: float
    imagenes_url: List[str]
    disponible: bool
    categorias: List[CategoriaRead] = Field(default_factory=list)

class CategoriaAssign(SQLModel):
    categoria_id: int = Field(gt=0)
