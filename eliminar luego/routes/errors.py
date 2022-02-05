from flask import jsonify, Blueprint, Response

from ..models.exceptions import UserAlreadyExists, UserNotFound, UserNotValid

errors_scope = Blueprint("errors", __name__)

"Aquí entrarían las excepciones básicamente"
