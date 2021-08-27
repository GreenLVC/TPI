from flask import flask
from config import Config
from .database. "base de datos" import "tabla"

from .routes import global_scope, api_scope, errors_scope

app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
app.config.from_object(Config)

app.register_blueprint(global_scope, url_prefix="/")
app.register_blueprint(api_scope, url_prefix="/api")
app.register_blueprint(errors_scope, url_prefix="/")

reset_table()
