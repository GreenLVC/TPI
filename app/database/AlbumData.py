import pymysql
from database.connection import DataBase
from models.models import Album
from typing import List, Optional


class AlbumData(DataBase):
    def __init__(self):
        super().__init__()

    def GetOne(self, id:int) -> Optional[Album]:
        self.open()
        try:
            self.cursor.execute(
                "select * from albums where id=%s ", id)
            a = Album(*self.cursor.fetchone().values())
            return a
        except:
            print("No se pudo recuperar el album.")
            self.connection.rollback()
            return None

        finally:
            self.cursor.close()
            self.close()

    def GetAll(self) -> List[Album]:
        self.open()
        listaAlbums = list()
        try:
            self.cursor.execute("select * from albums",)
            for al in self.cursor.fetchall():
                a = Album(*al.values())
                listaAlbums.append(a)
            return listaAlbums

        except:
            print("No se pudo recuperar el album.")
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.close()

    def Registrar(self, album: Album) -> bool:
        insertcmd = "insert into albums(nombre, fechaSalida) values (%s, %s)"
        self.open()
        try:
            self.cursor.execute(insertcmd, album.lst())
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.cursor.close()
            self.close()

    def Modificar(self, album: Album) -> bool:
        updt = "update albums set nombre= %s, fechaSalida= %s"
        params = (album.nombre, album.fechaSalida)
        self.open()
        try:
            self.cursor.execute(updt, params)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.cursor.close()
            self.connection.close()