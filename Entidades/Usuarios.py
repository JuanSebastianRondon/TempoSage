class Usuarios:
    def __init__(self, nombre:str="", edad:int=0, correo:str="",contraseña:str=""):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.contraseña = contraseña

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Correo: {self.correo}, Contraseña: {self.contraseña}"