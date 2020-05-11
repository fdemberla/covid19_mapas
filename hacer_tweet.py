from datetime import date
import time
from verificar_api import api
from obtener_imagenes import seleccionar_carpetas

fecha = date.today().strftime("%m/%Y")

imagenes = seleccionar_carpetas()


def obtener_dia():
    check = True

    while check:
        dia = input("Este tweet para que dia es?: ")
        if not int(dia):
            print("El valor introcido no es un numero!")
        else:
            confirmacion = input(
                f"El dia que introduciste es: {dia}/{fecha}, es esto correcto? (s/n): "
            )
            if confirmacion == "s":
                check = False
                return f"{dia}/{fecha}"
            else:
                break


fecha = obtener_dia()

# COVIDー19 #ProtegetePanama #QuedateEnCasa #CoronaVirusEnPanama #coronaviruspanama

tweet_anterior = ""

for imagen in imagenes:
    texto = f"""{imagen['nombre_completo']}
Actualizado {fecha}
#{imagen['nombre_completo'].replace(" ", "")} #COVIDー19 #ProtegetePanama #QuedateEnCasa #CoronaVirusEnPanama #coronaviruspanama"""
    tweet = api.update_with_media(
        imagen["ubicacion"],
        texto,
        in_reply_to_status_id=tweet_anterior,
        username="@covid19_mapas",
    )
    tweet_anterior = tweet._json.get("id")
    print(f"Tweet: {imagen['nombre_completo']}, ID: {tweet_anterior}, Realizado!")
    time.sleep(1)
