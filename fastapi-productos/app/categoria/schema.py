from typing import Optional
from pydantic import field_validator
from sqlmodel import SQLModel, Field

class CategoriaCreate(SQLModel):
    nombre: str = Field(min_length=1, max_length=100)
    descripcion: str = Field(default="", max_length=500)

    @field_validator("nombre")
    @classmethod
    def nombre_no_vacio(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("El nombre de la categoría no puede estar vacío")
        return value

class CategoriaUpdate(SQLModel):
    nombre: Optional[str] = Field(default=None, min_length=1, max_length=100)
    descripcion: Optional[str] = Field(default=None, max_length=500)

    @field_validator("nombre")
    @classmethod
    def nombre_no_vacio(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return value
        value = value.strip()
        if not value:
            raise ValueError("El nombre de la categoría no puede estar vacío")
        return value

class CategoriaRead(SQLModel):
    id: int
    nombre: str
    descripcion: str