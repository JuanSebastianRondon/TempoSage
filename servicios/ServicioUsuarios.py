from fastapi import FastAPI,APIRouter
from Entidades.Usuarios import Usuarios

router=APIRouter()
Usuario=Usuarios()
@router.get("/usuarios")
def get_usuarios():
    return Usuario.mostrar_informacion()

@router.get("/usuarios/{id}")
def get_usuario(id:int):
    if usuario.id==id:
        return Usuario.mostrar_informacion()
    else:
        return "Usuario no encontrado"

@router.post("/usuarios")
def create_usuario(nombre:str, edad:int, correo:str, contraseña:str):
    Usuario=Usuarios(nombre,edad,correo,contraseña)
    return Usuario.mostrar_informacion()

@router.put("/usuarios/{id}")
def update_usuario(id:int, nombre:str, edad:int, correo:str, contraseña:str):
    Usuario=Usuarios(nombre,edad,correo,contraseña)
    return Usuario.mostrar_informacion()

@router.delete("/usuarios/{id}")
def delete_usuario(id:int):
    return f"Usuario con id {id} eliminado"


