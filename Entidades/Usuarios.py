from pydantic import BaseModel
from typing import Optional as opcional

class Usuarios(BaseModel):
    id: opcional[str] = None
    nombre: opcional[str] = None
    correo: opcional[str] = None
    contraseña: opcional[str] = None
    