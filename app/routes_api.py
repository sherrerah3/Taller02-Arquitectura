from flask import Blueprint, jsonify
from .data import random_pokenea
from .utils import get_container_id

api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.get("/pokenea")
def get_random_pokenea_json():
    """
    Devuelve JSON con: id, nombre, altura, habilidad + container_id.
    """
    p = random_pokenea()
    payload = {
        "id": p["id"],
        "nombre": p["nombre"],
        "altura": p["altura"],
        "habilidad": p["habilidad"],
        "container_id": get_container_id(),
    }
    return jsonify(payload), 200
