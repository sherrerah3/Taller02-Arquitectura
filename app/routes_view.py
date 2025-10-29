from flask import Blueprint, render_template
from .data import random_pokenea
from .utils import get_container_id
from .aws_utils import get_image_url

view_bp = Blueprint("view", __name__)

@view_bp.get("/")
def home():
    """
    Muestra imagen + frase filosófica de un Pokenea aleatorio
    + el container_id en la vista.
    """
    p = random_pokenea()
    image_url = get_image_url(p["imagen"])
    return render_template(
        "pokenea.html",
        nombre=p["nombre"],
        imagen=image_url, 
        frase=p["frase"],
        container_id=get_container_id(),
    )
