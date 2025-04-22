from fastapi import FastAPI
from servicios.ServicioUsuarios import router

app=FastAPI()


app.include_router(router)

