"""Funciones de apoyo para los cuadernos de Introducción a OpenCV.

Acá vive solo lo accesorio: la configuración de las figuras de Matplotlib.
Todo lo que cambia qué se analiza o cómo se interpreta queda en los cuadernos.
"""
import matplotlib.pyplot as plt


def mostrar_imágenes(paneles, alto_de_figura=4):
    """Muestra varias imágenes una al lado de la otra.

    Recibe una lista de diccionarios. Cada diccionario describe un panel:
        {"imagen": arreglo de NumPy en RGB o en grises, "título": texto}

    Las imágenes de un solo canal se muestran en grises, con la escala fija
    de 0 a 255 para que dos paneles distintos sean comparables entre sí.
    """
    cantidad_de_paneles = len(paneles)
    ancho_de_figura = alto_de_figura * cantidad_de_paneles
    figura, ejes = plt.subplots(
        nrows=1,
        ncols=cantidad_de_paneles,
        figsize=(ancho_de_figura, alto_de_figura),
        squeeze=False,
    )
    ejes_disponibles = list(ejes[0])

    for panel in paneles:
        eje = ejes_disponibles.pop(0)
        imagen = panel["imagen"]
        if imagen.ndim == 2:
            eje.imshow(imagen, cmap="gray", vmin=0, vmax=255)
        else:
            eje.imshow(imagen)
        eje.set_title(panel["título"])
        eje.axis("off")

    figura.tight_layout()
    plt.show()


def mostrar_curvas(curvas, título, etiqueta_x, etiqueta_y):
    """Dibuja una o más curvas sobre los mismos ejes.

    Recibe una lista de diccionarios:
        {"valores": lista o arreglo de números, "nombre": texto para la leyenda}
    """
    figura, eje = plt.subplots(figsize=(10, 4))

    for curva in curvas:
        eje.plot(curva["valores"], label=curva["nombre"], linewidth=1.5)

    eje.set_title(título)
    eje.set_xlabel(etiqueta_x)
    eje.set_ylabel(etiqueta_y)
    eje.grid(alpha=0.3)
    eje.legend()
    figura.tight_layout()
    plt.show()
