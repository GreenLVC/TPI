import os
from dotenv import load_dotenv

load_dotenv()


class Config:
"""
    NOMBRE-SERVIDOR = "localhost:7001"
    //- [ ] El sistema debe estar **DESPLEGADO**
    - [ ] Debe estar online y accesible desde cualquier dispositivo, es decir no desde localhost (Sólo para Web)
    - [ ] En caso de no ser Web, debe poder installarse desde PyPi usando pip install//
     DEBUG = True
    
    pero a su vez dice

     [ ] Se utiliza una base de datos (MySQL, Mongo, SQLite)
     por lo que vamos a usar esta última regla y fué xd


    DATABASE_PATH: "app/database/contact_book.db" //aquí vá donde se encuentra la bd
    DB_TOKEN = os.environ.get("DB.TOKEN", "") # Para encriptar la DB
    ENCRYPT_DB = True
    
    TEMPLATE_FOLDER = "views/templates/" //aquí van lo de las plantillas
    STATIC_FOLDER = "views/static/"     //aquí va donde están los archivos estáticos
"""
