from typing import List

from database import AlbumData
from models.models import Album
from helpers import helper


class AlbumLogic:
    def __init__(self):
        self.datasource = AlbumData()

    def GetOne(self, ID:int) -> Optional[Album]:
        album=self.datasource.GetOne(ID)
        return album

    def GetAll(self) -> List[Album]:
        albums = self.datasource.GetAll()
        return albums
    
    def Registrar(self, album: Album) -> bool:
        self.datasource.Registrar(album)

    def Modificar(self, album: Album) -> bool:
        self.datasource.Modificar(album)