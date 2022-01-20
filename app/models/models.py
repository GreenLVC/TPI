from typing import NamedTuple, Optional

"""
programar todas las clases con sus atributos:

por ejemplo:

class Contact(NamedTuple):
    id: Optional[int] = None
    last_name: Optional[str] = None
    ... etc
    
"""

class Usuario(NamedTuple):
    id: Optional[int] = None
    alias: Optional[str] = None
    email: Optional[str] = None
    contrasenia: Optional[str] = None
    link_foto: Optional[str] = None
    cuenta_spotify: Optional[str] = None