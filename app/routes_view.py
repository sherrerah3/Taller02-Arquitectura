from flask import Blueprint, render_template
from .data import random_pokenea
from .utils import get_container_id

view_bp = Blueprint("view", __name__)

@view_bp.get("/")
def home():
    """
    Muestra imagen + frase filosófica de un Pokenea aleatorio
    + el container_id en la vista.
    """
    p = random_pokenea()
    return render_template(
        "pokenea.html",
        nombre=p["nombre"],
        imagen=p["imagen"],
        frase=p["frase"],
        container_id=get_container_id(),
    )
