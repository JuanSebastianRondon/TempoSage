from fastapi import FastAPI,APIRouter,HTTPException
from Entidades.preferencias import preferencias


router=APIRouter()
preferencia=preferencias()
prueba=[]
@router.get("/preferencia")
def get_preferencia():
    return prueba  #esto retorna una lista de preferencia cambialo por lo de la base

@router.get('/preferencia/{id}')
def get_preferencia(id:int):
    for preferencia in prueba:
        if preferencia["id"]==id:
            return preferencia
    raise HTTPException(status_code=404, detail="no hay nada bro") #esto retorna un preferencia por id cambialo por lo de la base y obvio lo busca en for PD:malditopython

@router.post("/preferencia")
def create_preferencia(preferencia:preferencias):
    preferencia.id=len(prueba)+1
    prueba.append(preferencia.dict()) #esta en la funcion que guarda el preferencia cabiala por la de la base
    return "recibido"

@router.put('/preferencia/{id}')
def update_preferencia(id:int, update_preferencia:preferencias):
    for i, preferencia in enumerate(prueba):
        if preferencia["id"] == id:
            prueba[i]["FrecuenciaNotificaciones"] = update_preferencia.FrecuenciaNotificaciones
            prueba[i]["ModoConcentracion"] = update_preferencia.ModoConcentracion
            return "actualizado"
    raise HTTPException(status_code=404, detail="no hay nada bro") #dentro del if actualiza el preferencia por id ya veras como lo haces en la base de datos
    
    

@router.delete("/preferencia/{id}")
def delete_preferencia(id:int):
    for i, preferencia in enumerate(prueba):
        if preferencia["id"] == id:
            prueba.pop(i)  # Elimina el preferencia de la lista
            return "eliminado"
    raise HTTPException(status_code=404, detail="preferencia no encontrado")