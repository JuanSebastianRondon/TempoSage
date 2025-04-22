from fastapi import FastAPI
from servicios.ServicioUsuarios import router as RutasUsuarios
from servicios.ServicioPreferencias import router as RutasPreferencias
from servicios.ServicioActividades import router as RutasActividades
from servicios.ServicioNotificaciones import router as RutasNotificaciones

app=FastAPI()


app.include_router(RutasUsuarios)
app.include_router(RutasPreferencias)
app.include_router(RutasActividades)
app.include_router(RutasNotificaciones)