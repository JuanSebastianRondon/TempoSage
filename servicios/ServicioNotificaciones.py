from fastapi import FastAPI,APIRouter,HTTPException
from Entidades.Notificaciones import Notificaciones


router=APIRouter()
notificacion=Notificaciones()
prueba=[]
@router.get("/notificacion")
def get_notificacion():
    return prueba  #esto retorna una lista de notificacion cambialo por lo de la base

@router.get('/notificacion/{id}')
def get_notificacion(id:int):
    for notificacion in prueba:
        if notificacion["id"]==id:
            return notificacion
    raise HTTPException(status_code=404, detail="no hay nada bro") #esto retorna un notificacion por id cambialo por lo de la base y obvio lo busca en for PD:malditopython

@router.post("/notificacion")
def create_notificacion(notificacion:Notificaciones):
    notificacion.id=len(prueba)+1
    prueba.append(notificacion.dict()) #esta en la funcion que guarda el notificacion cabiala por la de la base
    return "recibido"

@router.put('/notificacion/{id}')
def update_notificacion(id:int, update_notificacion:Notificaciones):
    for i, notificacion in enumerate(prueba):
        if notificacion["id"] == id:
            prueba[i]["mensaje"] = update_notificacion.mensaje
            prueba[i]["horaProgramada"] = update_notificacion.horaProgramada
            prueba[i]["estado"] = update_notificacion.estado
            return "actualizado"
    raise HTTPException(status_code=404, detail="no hay nada bro") #dentro del if actualiza el notificacion por id ya veras como lo haces en la base de datos
    
    

@router.delete("/notificacion/{id}")
def delete_notificacion(id:int):
    for i, notificacion in enumerate(prueba):
        if notificacion["id"] == id:
            prueba.pop(i)  # Elimina el notificacion de la lista
            return "eliminado"
    raise HTTPException(status_code=404, detail="notificacion no encontrado")