import random

POKENEAS = [
    {
        "id": 1,
        "nombre": "Neachu",
        "altura": 0.9,
        "habilidad": "Doble maíz",
        "imagen": "https://example.com/arepachu.png",
        "frase": "Un toquesito o que?"
    },
    {
        "id": 2,
        "nombre": "Bulbasureño",
        "altura": 1.2,
        "habilidad": "Vitaminazo",
        "imagen": "https://example.com/guayabion.png",
        "frase": "Soy del verde soy feliz"
    },
    {
        "id": 3,
        "nombre": "Charmanea",
        "altura": 1.6,
        "habilidad": "Desfile floral",
        "imagen": "https://example.com/silletron.png",
        "frase": "Con guayaba y verraquera se puede"
    },
    {
        "id": 4,
        "nombre": "Chorizord",
        "altura": 1.1,
        "habilidad": "Subida eterna",
        "imagen": "https://example.com/trotamonte.png",
        "frase": "Pa arriba es que vamos pues."
    },
    {
        "id": 5,
        "nombre": "Squirtle",
        "altura": 1.4,
        "habilidad": "Aroma vital",
        "imagen": "https://example.com/cafesaurio.png",
        "frase": "Un tintico y sale"
    },
    {
        "id": 6,
        "nombre": "Rattota",
        "altura": 0.7,
        "habilidad": "Energía paisa",
        "imagen": "https://example.com/bandejin.png",
        "frase": "Poropopo, poropopo el que no salte es un rolo mari***"
    },
    {
        "id": 7,
        "nombre": "Metapai",
        "altura": 2.1,
        "habilidad": "Desplazamiento limpio",
        "imagen": "https://example.com/metrovol.png",
        "frase": "Jueves de palmas"
    },
    {
        "id": 8,
        "nombre": "Butterfresa",
        "altura": 1.0,
        "habilidad": "Verde urbano",
        "imagen": "https://example.com/parquebot.png",
        "frase": "2 pa 2 o que?"
    },
    {
        "id": 9,
        "nombre": "Parcean",
        "altura": 0.8,
        "habilidad": "Energía renovable",
        "imagen": "https://example.com/solarpika.png",
        "frase": "El que se asusta se quema"
    },
    {
        "id": 10,
        "nombre": "Slowbroki",
        "altura": 1.3,
        "habilidad": "Sabor tradicional",
        "imagen": "https://example.com/arepajiggly.png",
        "frase": "Mas que mi hermano eres mi bro."
    }
]

def random_pokenea():
    return random.choice(POKENEAS)
