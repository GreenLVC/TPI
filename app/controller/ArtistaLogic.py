from typing import List
from database import ArtistaData
from models.models import Artista
from helpers import helper


class ArtistaLogic:
    def __init__(self):
        self.datasource = ArtistaData()

    def GetOne(self, ID:int) -> Optional[Artista]:
        artista=self.datasource.GetOne(ID)
        return artista

    def GetAll(self) -> List[Artista]:
        artistas = self.datasource.GetAll()
        return artistas
    
    def Registrar(self, artista: Artista) -> bool:
        self.datasource.Registrar(artista)

    def Modificar(self, artista: Artista) -> bool:
        self.datasource.Modificar(artista)