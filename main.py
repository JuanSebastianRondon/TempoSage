from fastapi import FastAPI
from servicios.ServicioUsuarios import router

app=FastAPI()

def main():
    app.include_router(router)

if __name__== "__main__":
    main() 