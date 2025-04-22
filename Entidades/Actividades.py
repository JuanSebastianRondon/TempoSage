from pydantic import BaseModel, Field
from typing import Optional as opcional
from datetime import datetime

class Actividades(BaseModel):
    id: opcional[str] = None
    titulo: opcional[str] = None
    descripcion: opcional[str] = None  
    fechaInicio:datetime = Field(default_factory=datetime.now)
    fechaFin: opcional[datetime] = None
    prioridad: opcional[int] = None
    categoria: opcional[str] = None
    color: opcional[str] = None