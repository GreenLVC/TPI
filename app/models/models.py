from typing import NamedTuple, Optional
from datetime import date, time

"""
programar todas las clases con sus atributos:

por ejemplo:


    
"""

class Album():
    def __init__(self, id: int, nombre: str, fechaSalida: date) -> None:
        self.id = id
        self.nombre = nombre
        self.fechaSalida = fechaSalida

    def lst(self) -> tuple:
        return self.id ,self.nombre, self.fechaSalida


class Artista():
    def __init__(self, id:int, nombre: str, popularidad: float, tipo_artista: str) -> None:
        self.id = id
        self.nombre = nombre
        self.popularidad = popularidad
        self.tipo_artista = tipo_artista

    def lst(self) -> tuple:
        return self.id, self.nombre, self.popularidad, self.tipo_artista

class Cancion():
    def __init__(self, id:int, titulo:str, pista:str, mood:str, duracion: time, reproducciones: int, 
    explicita: bool, popularidad: float, tipo_cancion: str, idAlbum: int) -> None:
        self.id = id
        self.titulo = titulo
        self.pista = pista
        self.mood = mood
        self.duracion = duracion
        self.reproducciones = reproducciones
        self.explicita = explicita
        self.popularidad = popularidad
        self.tipo_cancion = tipo_cancion
        self.idAlbum = idAlbum
    
    def lst(self) -> tuple:
        return self.id, self.titulo, self.pista, self.mood, self.duracion, self.reproducciones, self.explicita,
        self.popularidad, self.tipo_cancion, self.idAlbum

class Cuenta():
    def __init__(self, id:int, email: str, explicito:bool, display_name:str, tipo_cuenta:str) -> None:
        self.id = id
        self.email = email
        self.explicito = explicito
        self.display_name = display_name
        self.tipo_cuenta = tipo_cuenta

    def lst(self) -> tuple:
        return self.id, self.email, self.explicito, self.display_name, self.tipo_cuenta

class Genero_Cancion():
    def __init__(self, id:int, id_artista: int, id_cancion: int, id_genero: int, 
    artista_principal:bool, fecha_publicacion: date) -> None:
        self.id = id
        self.id_artista= id_artista
        self.id_cancion = id_cancion
        self.id_genero = id_genero
        self.artista_principal = artista_principal
        self.fecha_publicacion = fecha_publicacion

    def lst(self) -> tuple:
        return self.id, self.id_artista, self.id_cancion, self.id_genero, 
        self.artista_principal, self.fecha_publicacion
    
class Genero():
    def __init__(self, id:int, nombre:str, descripcion:str, id_sub_genero:int) ->None:
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.id_sub_genero = id_sub_genero

    def lst(self) -> tuple:
        return self.id, self.nombre, self.descripcion, self.id_sub_genero

class Playlist_Cancion():
    def __init__(self, id: int, id_playlist:int, id_cancion:int, total:int, limite:int) -> None:
        self.id = id
        self.id_playlist = id_playlist
        self.id_cancion = id_cancion
        self.total = total
        self.limite = limite

    def lst(self) -> tuple:
        return self.id, self.id_playlist, self.id_cancion, self.total, self.limite

class Playlist():
    def __init__(self, id:int, nombre:str, fecha_creacion:date, privacidad:bool) -> None:
        self.id = id
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion
        self.privacidad = privacidad

    def lst(self) -> tuple:
        return self.id, self.nombre, self.fecha_creacion, self.privacidad

class UsuarioPlaylist():
    def __init__(self, id:int, id_usuario:int, id_playlist:int, tipo_usuario:str, fecha_uso:date, fecha_modificacion:date, fecha_eliminacion:date)-> None:
        self.id = id
        self.id_usuario = id_usuario
        self.id_playlist = id_playlist
        self.tipo_usuario = tipo_usuario
        self.fecha_uso = fecha_uso
        self.fecha_eliminacion = fecha_eliminacion
        self.fecha_modificacion = fecha_modificacion

    def lst(self) -> tuple:
        return self.id, self.id_usuario, self.id_playlist, self.tipo_usuario, self.fecha_uso, self.fecha_modificacion, self.fecha_eliminacion

class Usuario():
    def __init__(self, id:int, alias:str, contrasenia:str, foto_perfil:str, pais:str, id_cuenta: int, email:str) -> None:
        self.id = id
        self.alias = alias
        self.contrasenia = contrasenia
        self.foto_perfil = foto_perfil
        self.pais = pais
        self.id_cuenta = id_cuenta
        self.email = email

    def lst(self) -> tuple:
        return self.id, self.alias, self.contrasenia, self.foto_perfil, self.pais, self.id_cuenta, self.email
