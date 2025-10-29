from flask import Blueprint, jsonify, render_template, request
from .data import random_pokenea
from .utils import get_container_id

api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.get("/pokenea")
def get_random_pokenea_json():
    """
    Devuelve JSON con: id, nombre, altura, habilidad + container_id.
    Si se accede desde navegador (Accept: text/html), renderiza vista HTML.
    Si se accede como API (Accept: application/json), devuelve JSON.
    """
    p = random_pokenea()
    payload = {
        "id": p["id"],
        "nombre": p["nombre"],
        "altura": p["altura"],
        "habilidad": p["habilidad"],
        "container_id": get_container_id(),
    }
    
    # Detectar si es petición desde navegador
    if request.accept_mimetypes.best_match(['text/html', 'application/json']) == 'text/html':
        return render_template("json_viewer.html")
    
    return jsonify(payload), 200
