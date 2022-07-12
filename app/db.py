from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import *


class Datos:
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:1234@localhost/myplaylists')
        Base.metadata.bind = self.engine
        db_session = sessionmaker()
        db_session.bind = self.engine
        self.session = db_session()

    def creaTabla(self):
        Base.metadata.create_all(self.engine)  # Crea la tabla socios


class DatosAlbum(Datos):

    def buscar(self, id_socio: int):
        return self.session.query(Album).filter(Album.id == id_socio).first()

    def todos(self) -> List[Album]:
        return self.session.query(Album).all()

    def borrar_todos(self) -> bool:
        albums = self.todos()
        if not albums:
            return False
        for alb in albums:
            self.baja(alb.id)
        return True

    def alta(self, album: Album) -> Album:
        self.session.add(album)
        self.session.commit()
        return album

    def baja(self, id_album: int) -> bool:
        album = self.buscar(id_album)
        if album is None:
            return False
        self.session.delete(album)
        self.session.commit()
        return True

    def modificacion(self, album: Album) -> Album:
        self.session.query(Album).filter(Album.id == album.id).update(
            {Album.nombre: album.nombre, Album.fecha_salida: album.fecha_salida})
        self.session.commit()
        return album

    def contarAlbums(self) -> int:
        a = self.session.query(Album).count()
        return a


class DatosUsuarios(Datos):

    def buscar(self, usuario:Usuario):
        return self.session.query(Usuario).filter(Usuario.email == usuario.email and
                                                  Usuario.password == usuario.contrasenia).first()

    def alta(self, user: Usuario) -> Usuario:
        self.session.add(user)
        self.session.commit()
        return user


if __name__ == '__main__':
    datos = Datos()
    # Ejecutar db.py en caso de que se requiera crear la base de datos

    datos.creaTabla()
