from typing import Optional
from sqlmodel import SQLModel

class CategoriaCreate(SQLModel):
    nombre: str
    descripcion: str

class CategoriaUpdate(SQLModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None

class CategoriaRead(SQLModel):
    id: int
    nombre: str
    descripcion: str