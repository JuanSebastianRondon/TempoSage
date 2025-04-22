from fastapi import FastAPI,APIRouter,HTTPException
from Entidades.Usuarios import Usuarios


router=APIRouter()
Usuario=Usuarios()
prueba=[]
@router.get("/usuarios")
def get_usuarios():
    return prueba  #esto retorna una lista de usuarios cambialo por lo de la base

@router.get('/usuarios/{id}')
def get_usuario(id:int):
    for Usuario in prueba:
        if Usuario["id"]==id:
            return Usuario
    raise HTTPException(status_code=404, detail="no hay nada bro") #esto retorna un usuario por id cambialo por lo de la base y obvio lo busca en for PD:malditopython

@router.post("/usuarios")
def create_usuario(usuario:Usuarios):
    usuario.id=len(prueba)+1
    prueba.append(usuario.dict()) #esta en la funcion que guarda el usuario cabiala por la de la base
    return "recibido"

@router.put('/usuarios/{id}')
def update_usuario(id:int, update_usuario:Usuarios):
    for i, usuario in enumerate(prueba):
        if usuario["id"] == id:
            prueba[i]["nombre"] = update_usuario.nombre
            prueba[i]["correo"] = update_usuario.correo
            prueba[i]["contraseña"] = update_usuario.contraseña
            return "actualizado"
    raise HTTPException(status_code=404, detail="no hay nada bro") #dentro del if actualiza el usuario por id ya veras como lo haces en la base de datos
    
    

@router.delete("/usuarios/{id}")
def delete_usuario(id:int):
    for i, usuario in enumerate(prueba):
        if usuario["id"] == id:
            prueba.pop(i)  # Elimina el usuario de la lista
            return "eliminado"
    raise HTTPException(status_code=404, detail="Usuario no encontrado")



