# Importar paquetes
import os

carpetas = os.listdir(f"{os.getcwd()}\mapas")

lista_de_provincias = [
    {"nombre_completo": "Bocas del Toro", "nomenclatura": "BOC"},
    {"nombre_completo": "Comarca Emberá", "nomenclatura": "CE"},
    {"nombre_completo": "Chiriquí", "nomenclatura": "CH"},
    {"nombre_completo": "Coclé", "nomenclatura": "COCL"},
    {"nombre_completo": "Colón", "nomenclatura": "COL"},
    {"nombre_completo": "Darién", "nomenclatura": "DAR"},
    {"nombre_completo": "Comarca Guna Yala", "nomenclatura": "GY"},
    {"nombre_completo": "Herrera", "nomenclatura": "HER"},
    {"nombre_completo": "Los Santos", "nomenclatura": "LS"},
    {"nombre_completo": "Ngäbe-Buglé", "nomenclatura": "NB"},
    {"nombre_completo": "Panamá Centro", "nomenclatura": "PC"},
    {"nombre_completo": "Panamá Este", "nomenclatura": "PE"},
    {"nombre_completo": "Panamá Norte", "nomenclatura": "PN"},
    {"nombre_completo": "Panamá Oeste", "nomenclatura": "PO"},
    {"nombre_completo": "San Miguelito", "nomenclatura": "SM"},
    {"nombre_completo": "Veraguas", "nomenclatura": "VER"},
]

lista_de_totales = [
    {"nombre_completo": "Distribucion Geografica de Casos", "nomenclatura": "TOT1"},
    {"nombre_completo": "Casos Nuevos por Fecha", "nomenclatura": "TOT2"},
    {"nombre_completo": "Total de Casos por Fecha", "nomenclatura": "TOT3"},
    {
        "nombre_completo": "Total de casos y fallecidos por rango de edad",
        "nomenclatura": "TOT4",
    },
    {
        "nombre_completo": "Distribucion Geografica de Recuperados",
        "nomenclatura": "TOT5",
    },
    {
        "nombre_completo": "Distribucion Geografica de Fallecidos",
        "nomenclatura": "TOT6",
    },
]


def obtener_archivos(directorio, lista_verificacion):

    nueva_lista = []

    for imagen in os.listdir(directorio):
        ind = [i for i, s in enumerate(os.listdir(directorio)) if imagen in s]
        objeto = {
            "nombre_completo": lista_verificacion[ind[0]]["nombre_completo"],
            "ubicacion": directorio + fr"\{imagen}",
        }
        nueva_lista.append(objeto)

    return nueva_lista


# COMENTARIO PARA MOSTRAR GITHUB


def seleccionar_carpetas():

    # Obtener lista de carpetas
    print("Escoje la carpeta de los mapas: ")
    print("Indice\t||\tNombre de Carpeta")
    print("-" * 30)

    indice = 0
    for carpeta in carpetas:
        indice += 1
        print(f"   {indice}\t||\t\t{carpeta}")
    print("*" * 30)

    carpeta_seleccionada = input("Seleccione la carpeta: ")

    try:
        value = int(carpeta_seleccionada) - 1

        print("_" * 30)
        print("1. Regiones\n2. Totales")
        print("_" * 30)

        sel_tweet = input("Que tweet vas a hacer?: ")

        if sel_tweet == "1":
            return obtener_archivos(
                fr"""{os.getcwd()}\mapas\{carpetas[value]}\Regiones""",
                lista_de_provincias,
            )
        elif sel_tweet == "2":
            return obtener_archivos(
                fr"""{os.getcwd()}\mapas\{carpetas[value]}\Totales""", lista_de_totales
            )
        else:
            print("Valor Incorrecto")
            return None

    except ValueError:
        print("Eso no es un numero!")
