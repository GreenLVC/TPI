import pymysql
from database.connection import DataBase
from models.models import Artista
from typing import List, Optional


class ArtistaData(DataBase):
    def __init__(self):
        super().__init__()

    def GetOne(self, id:int) -> Optional[Artista]:
        self.open()
        try:
            self.cursor.execute(
                "select * from artistas where id=%s", id)
            a = Artista(*self.cursor.fetchone().values())
            return a
        except:
            print("No se pudo recuperar el artista.")
            self.connection.rollback()
            return None

        finally:
            self.cursor.close()
            self.close()

    def GetAll(self) -> List[Artista]:
        self.open()
        listaArtista = list()
        try:
            self.cursor.execute("select * from artistas",)
            for art in self.cursor.fetchall():
                a = Artista(*usu.values())
                listaArtista.append(a)
            return listaArtista

        except:
            print("No se pudo recuperar el artista.")
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.close()

    def Registrar(self, artista: Artista) -> bool:
        insertcmd = "insert into artistas(nombre, popularidad, tipo_artista) values (%s, %s, %s)"
        self.open()
        try:
            self.cursor.execute(insertcmd, artista.lst())
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.cursor.close()
            self.close()

    def Modificar(self, artista: Artista) -> bool:
        updt = "update artistas set nombre= %s, popularidad= %s, tipo_artista= %s"
        params = (artista.nombre, artista.popularidad, artista.tipo_artista)
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