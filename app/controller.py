from app.db import *


class NegocioUsuario:

    def __init__(self):
        self.datos = DatosUsuarios()

    def buscar(self, negocio):
        return self.datos.buscar(negocio)

    def alta(self, user: Usuario):
        try:
            self.datos.alta(user)
        except Exception as ex:
            raise ex


class NegocioAlbum:

    def __init__(self):
        self.datos = DatosAlbum()

    def buscar(self, id_album: int):
        return self.datos.buscar(id_album)

    def todos(self) -> List[Album]:
        return self.datos.todos()
