from typing import List
from ..database import UsuarioData
from app.models.models import Usuario


class UsuarioLogic:
    def __init__(self):
        self.datasource = UsuarioData()

    def GetOne(self, email:str, contrasenia: str) -> Usuario:
        usuario=self.datasource.GetOne(email, contrasenia)
        return usuario

    def GetAll(self) -> List[Usuario]:
        usuarios = self.datasource.GetAll()
        return usuarios
    
    def Registrar(self, user: Usuario) -> bool:
        self.datasource.Registrar(user)

    def Modificar(self, user: Usuario) -> bool:
        self.datasource.Modificar(user)