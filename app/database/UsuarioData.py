import pymysql
from app.database.connection import DataBase
from app.models.models import Usuario
from typing import List, Optional
from flask_login import UserMixin


class UsuarioData(DataBase, UserMixin):
    def __init__(self):
        super().__init__()

    def GetOne(self, nombre:str , contrasenia:str) -> Optional[Usuario]:
        self.open()
        try:
            self.cursor.execute(
                "select * from usuarios where email=%s and contrasenia =%s", email, contrasenia)
            u = Usuarios(*self.cursor.fetchone().values())
            return u
        except:
            print("No se pudo recuperar el usuario.")
            self.connection.rollback()
            return None

        finally:
            self.cursor.close()
            self.close()

    def GetAll(self) -> List[Usuario]:
        self.open()
        listaUsuarios = list()
        try:
            self.cursor.execute("select * from usuarios",)
            for usu in self.cursor.fetchall():
                u = Usuarios(*usu.values())
                listaUsuarios.append(u)
            return listaUsuarios

        except:
            print("No se pudo recuperar el usuario.")
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.close()

    def Registrar(self, usuario: Usuario) -> bool:
        insertcmd = "insert into usuarios(alias, contrasenia, foto_perfil, pais, idCuenta) values (%s, %s, %s, %s, %s)"
        self.open()
        try:
            self.cursor.execute(insertcmd, usuario.lst())
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.cursor.close()
            self.close()

    def Modificar(self, user: Usuario) -> bool:
        updt = "update usuarios set contrasenia= %s, alias= %s, foto_perfil= %s, pais= %s , idCuenta =%s where alias= %s and contrasenia =%"
        params = (user.contrasenia, user.alias,
                  user.foto_perfil, user.pais, user.id_cuenta, user.alias, user.contrasenia)
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