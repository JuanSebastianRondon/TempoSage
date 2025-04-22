from pydantic import BaseModel, Field
from typing import Optional as opcional
from datetime import datetime

class Notificaciones(BaseModel):
    id: opcional[str] = None
    mensaje: opcional[str] = None
    horaProgramada: opcional[datetime] = None
    estado:bool = False #lo deje boleano proque manejarlo es str despues va hacer conplicado y ademas cuantos estados puede tener
    