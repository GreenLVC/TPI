from flask import Blueprint, render_template

global_scope = Blueprint("vies", __name__)

"""
aquí habría que declarar todos los objetos que vamos a utilizar, algunos ejemplos:

nav = [
    {"name": "Listar Todos", "url": "/api/contacts"},
    {"name": "Contacto ID 1", "url": "/api/contacts/1"},
]


@global_scope.route("/", methods=['GET'])
def home():
    ""Landing page route.""

    parameters = {"title": "Flask and Jinja Practical work",
                  "description": "This is a simple page made for implement the basics concepts of Flask and Jinja2"
                  }

    return render_template("home.html", nav=nav, **parameters)
    
    
"""