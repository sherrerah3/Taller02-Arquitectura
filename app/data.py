import random

POKENEAS = [
    {
        "id": 1,
        "nombre": "Neachu",
        "altura": 0.9,
        "habilidad": "Doble maíz",
        "imagen": "Neachu.png",
        "frase": "Un toquesito o qué mi papa?"
    },
    {
        "id": 2,
        "nombre": "Bulbasureño",
        "altura": 1.2,
        "habilidad": "Vitaminazo",
        "imagen": "Bulbasureño.png",
        "frase": "Soy del verde soy feliz, y por el verde me doy puño con el que sea"
    },
    {
        "id": 3,
        "nombre": "Charmanea",
        "altura": 1.6,
        "habilidad": "Desfile floral",
        "imagen": "Charmanea.png",
        "frase": "Con guayaba y verraquera se puede"
    },
    {
        "id": 4,
        "nombre": "Chorizord",
        "altura": 1.1,
        "habilidad": "Subida eterna",
        "imagen": "Chorizord.png",
        "frase": "Pa arriba es que vamos pues."
    },
    {
        "id": 5,
        "nombre": "Squirtle",
        "altura": 1.4,
        "habilidad": "Aroma vital",
        "imagen": "Squirtle.png",
        "frase": "Un tintico y sale"
    },
    {
        "id": 6,
        "nombre": "Rattota",
        "altura": 0.7,
        "habilidad": "Energía paisa",
        "imagen": "Rattota.png",
        "frase": "Poropopo, poropopo el que no salte es un rolo mari***"
    },
    {
        "id": 7,
        "nombre": "Metapai",
        "altura": 2.1,
        "habilidad": "Desplazamiento limpio",
        "imagen": "Metapai.png",
        "frase": "Jueves de palmas"
    },
    {
        "id": 8,
        "nombre": "Butterfresa",
        "altura": 1.0,
        "habilidad": "Verde urbano",
        "imagen": "Butterfresa.png",
        "frase": "2 pa 2 o que?"
    },
    {
        "id": 9,
        "nombre": "Slowbroki",
        "altura": 0.8,
        "habilidad": "Energía renovable",
        "imagen": "Slowbroki.png",
        "frase": "El que se asusta se quema"
    },
    {
        "id": 10,
        "nombre": "Dunsparcero",
        "altura": 1.3,
        "habilidad": "Sabor tradicional",
        "imagen": "Dunsparcero.png",
        "frase": "Mas que mi hermano eres mi bro."
    }
]

def random_pokenea():
    return random.choice(POKENEAS)
