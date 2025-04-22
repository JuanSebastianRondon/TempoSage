from pydantic import BaseModel, Field
from typing import Optional as opcional
from datetime import datetime

class preferencias(BaseModel):
    id: opcional[str] = None
    FrecuenciaNotificaciones: opcional[int] = None
    ModoConcentracion:bool = False
    Inicio:datetime = Field(default_factory=datetime.now)
    Fin: opcional[datetime] = None
