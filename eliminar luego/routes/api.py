from flask import Blueprint, request, jsonify, redirect, url_for

from ..controller import contacts_controller
from ..models.models import Contact


api_scope = Blueprint("api", __name__)
