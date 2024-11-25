import random

def generar_cartas_monstruo():
    tipos_monstruo = {
        "L": "Lanzador de Conjuros",
        "D": "Dragón",
        "Z": "Zombi",
        "G": "Guerrero",
        "B": "Bestia",
        "O": "Demonio"
    }
    atributos = ["OSCURIDAD", "LUZ", "TIERRA", "AGUA", "FUEGO", "VIENTO"]
    nombres_base = ["Guerrero", "Dragón", "Zombi", "Mago", "Bestia", "Demonio"]
    descripciones_base = [
        "Un ser formidable que domina el campo de batalla.",
        "Una criatura temible con poderes ancestrales.",
        "Un espíritu implacable que no se detiene ante nada.",
        "Un maestro de la magia que controla los elementos.",
        "Una criatura salvaje con fuerza inigualable.",
        "Un ser oscuro que siembra el caos a su paso."
    ]
    
    cartas = []
    for _ in range(100): 
        tipo = random.choice(list(tipos_monstruo.keys()))
        atributo = random.choice(atributos)
        ataque = random.randint(500, 3000)
        defensa = random.randint(500, 3000)
        nombre = f"{random.choice(nombres_base)} de {atributo.capitalize()}"
        descripcion = random.choice(descripciones_base)
        cartas.append(f"{nombre},{descripcion},Monstruo,{ataque},{defensa},{tipo},{atributo}")
    return cartas

import random

def generar_cartas_trampa():
    atributos = ["OSCURIDAD", "LUZ", "TIERRA", "AGUA", "FUEGO", "VIENTO"]
    nombres_base = [
        "Tornado de Polvo", "Barricada Mágica", "Espejo Oscuro",
        "Muralla de Agua", "Fuego Purificador", "Torbellino Aéreo"
    ]
    efectos_base = [
        "detiene el ataque de un monstruo con tipo de atributo"
    ]
    
    cartas = []
    while len(cartas) < 50: 
        atributo = random.choice(atributos)
        nombre = f"{random.choice(nombres_base)} de {atributo}"
        descripcion = f"{nombre}, {random.choice(efectos_base)} {atributo}."
        cartas.append(f"{nombre},{descripcion},Trampa,{atributo}")
    
    return cartas


import random

def generar_cartas_magicas():
    nombres_base = [
        "Espada de Arturo", "Martillo de Thor", "Báculo de Ra",
        "Llama Infernal", "Escudo de Atenea", "Cloak of Shadows"
    ]
    
    # Tipos de monstruo disponibles
    tipos_monstruo = {
        "L": "Lanzador de Conjuros",
        "D": "Dragón",
        "Z": "Zombi",
        "G": "Guerrero",
        "B": "Bestia",
        "O": "Demonio"
    }
    efectos_base = [
        "incrementa en {0} el ataque de monstruos de tipo {1}",
        "reduce en {0} el ataque de monstruos de tipo {1}",
        "aumenta en {0} la defensa de monstruos de tipo {1}"
    ]
    
    cartas = []
    while len(cartas) < 50:
        nombre = random.choice(nombres_base)
        tipo_monstruo = random.choice(list(tipos_monstruo.values()))
        efecto = random.choice(efectos_base)
        incremento = random.randint(100, 500)
        descripcion = efecto.format(incremento, tipo_monstruo)
        tipo_inicial = list(tipos_monstruo.keys())[list(tipos_monstruo.values()).index(tipo_monstruo)]
        cartas.append(f"{nombre},{descripcion},Mágica,{tipo_inicial},{incremento},{'ataque' if 'ataque' in descripcion else 'defensa'}")
    
    return cartas


def guardar_cartas(cartas, ruta_archivo):
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(cartas))  


