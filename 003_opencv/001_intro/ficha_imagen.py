# ────────────────────────────────────────────────
# ficha_imagen.py
# Genera la ficha técnica de una imagen y guarda una copia anotada.
# Uso: python ficha_imagen.py ruta/de/la/imagen.jpg
# ────────────────────────────────────────────────
import sys
from pathlib import Path

import cv2

CARPETA_SALIDAS = Path("salidas")


def obtener_ruta_de_la_imagen():
    """Lee la ruta de la imagen desde la línea de comandos o muestra cómo usar el script."""
    if len(sys.argv) < 2:
        print("Uso: python ficha_imagen.py ruta/de/la/imagen.jpg")
        sys.exit(1)
    ruta_de_la_imagen = Path(sys.argv[1])
    return ruta_de_la_imagen


def leer_imagen_rgb(ruta_de_la_imagen):
    """Lee una imagen con OpenCV, verifica la lectura y la devuelve en RGB."""
    imagen_leída = cv2.imread(filename=str(ruta_de_la_imagen), flags=cv2.IMREAD_COLOR)
    assert imagen_leída is not None, f"No se pudo leer: {ruta_de_la_imagen}"
    imagen_convertida = cv2.cvtColor(src=imagen_leída, code=cv2.COLOR_BGR2RGB)
    return imagen_convertida


def construir_ficha(ruta_de_la_imagen, imagen_rgb):
    """Devuelve un diccionario con los datos técnicos principales de una imagen ya leída."""
    imagen_gris = cv2.cvtColor(src=imagen_rgb, code=cv2.COLOR_RGB2GRAY)
    peso_en_kb = ruta_de_la_imagen.stat().st_size / 1024
    brillo_medio = imagen_gris.mean()
    ficha = {
        "archivo": ruta_de_la_imagen.name,
        "peso_kb": round(peso_en_kb, 1),
        "ancho_x_alto": f"{imagen_rgb.shape[1]} x {imagen_rgb.shape[0]}",
        "brillo_medio": round(brillo_medio, 1),
    }
    return ficha


def preparar_imagen_de_trabajo(imagen_rgb, ancho_objetivo):
    """Redimensiona la imagen a un ancho fijo conservando su proporción."""
    alto_original = imagen_rgb.shape[0]
    ancho_original = imagen_rgb.shape[1]
    alto_objetivo = round(alto_original * ancho_objetivo / ancho_original)
    if ancho_objetivo < ancho_original:
        interpolación = cv2.INTER_AREA
    else:
        interpolación = cv2.INTER_CUBIC
    imagen_de_trabajo = cv2.resize(src=imagen_rgb, dsize=(ancho_objetivo, alto_objetivo), interpolation=interpolación)
    return imagen_de_trabajo


def anotar_ficha(imagen_rgb, ficha):
    """Devuelve una copia de la imagen con cada campo de la ficha escrito en una franja negra."""
    imagen_anotada = imagen_rgb.copy()
    posición_vertical = 40
    for campo in ficha:
        valor = ficha[campo]
        línea_de_texto = f"{campo}: {valor}"
        cv2.rectangle(img=imagen_anotada, pt1=(10, posición_vertical - 28), pt2=(430, posición_vertical + 10), color=(0, 0, 0), thickness=-1)
        cv2.putText(img=imagen_anotada, text=línea_de_texto, org=(20, posición_vertical), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.7, color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
        posición_vertical = posición_vertical + 38
    return imagen_anotada


def guardar_imagen_rgb(imagen_rgb, ruta_de_salida):
    """Convierte una imagen RGB a BGR y la guarda, creando la carpeta si hace falta."""
    ruta_de_salida.parent.mkdir(exist_ok=True)
    imagen_bgr = cv2.cvtColor(src=imagen_rgb, code=cv2.COLOR_RGB2BGR)
    se_guardó = cv2.imwrite(filename=str(ruta_de_salida), img=imagen_bgr)
    assert se_guardó, f"No se pudo guardar: {ruta_de_salida}"


def mostrar_ficha(ficha):
    """Imprime cada campo de la ficha en una línea."""
    for campo in ficha:
        valor = ficha[campo]
        print(f"{campo:<18}{valor}")


if __name__ == "__main__":
    ruta_de_la_imagen = obtener_ruta_de_la_imagen()
    imagen_rgb = leer_imagen_rgb(ruta_de_la_imagen)
    ficha = construir_ficha(ruta_de_la_imagen=ruta_de_la_imagen, imagen_rgb=imagen_rgb)
    imagen_de_trabajo = preparar_imagen_de_trabajo(imagen_rgb=imagen_rgb, ancho_objetivo=800)
    imagen_anotada = anotar_ficha(imagen_rgb=imagen_de_trabajo, ficha=ficha)
    ruta_de_salida = CARPETA_SALIDAS / f"ficha_{ruta_de_la_imagen.stem}.png"
    guardar_imagen_rgb(imagen_rgb=imagen_anotada, ruta_de_salida=ruta_de_salida)
    mostrar_ficha(ficha=ficha)
    print(f"Imagen anotada guardada en: {ruta_de_salida}")
