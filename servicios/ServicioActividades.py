from fastapi import FastAPI,APIRouter,HTTPException
from Entidades.Actividades import Actividades


router=APIRouter()
actividad=Actividades()
prueba=[]
@router.get("/actividad")
def get_actividad():
    return prueba  #esto retorna una lista de actividad cambialo por lo de la base

@router.get('/actividad/{id}')
def get_actividad(id:int):
    for actividad in prueba:
        if actividad["id"]==id:
            return actividad
    raise HTTPException(status_code=404, detail="no hay nada bro") #esto retorna un actividad por id cambialo por lo de la base y obvio lo busca en for PD:malditopython

@router.post("/actividad")
def create_actividad(actividad:Actividades):
    actividad.id=len(prueba)+1
    prueba.append(actividad.dict()) #esta en la funcion que guarda el actividad cabiala por la de la base
    return "recibido"

@router.put('/actividad/{id}')
def update_actividad(id:int, update_actividad:Actividades):
    for i, actividad in enumerate(prueba):
        if actividad["id"] == id:
            prueba[i]["titulo"] = update_actividad.titulo
            prueba[i]["descripcion"] = update_actividad.descripcion
            prueba[i]["prioridad"] = update_actividad.prioridad
            prueba[i]["categoria"] = update_actividad.categoria
            prueba[i]["color"] = update_actividad.color
            return "actualizado"
    raise HTTPException(status_code=404, detail="no hay nada bro") #dentro del if actualiza el actividad por id ya veras como lo haces en la base de datos
    
    

@router.delete("/actividad/{id}")
def delete_actividad(id:int):
    for i, actividad in enumerate(prueba):
        if actividad["id"] == id:
            prueba.pop(i)  # Elimina el actividad de la lista
            return "eliminado"
    raise HTTPException(status_code=404, detail="actividad no encontrado")