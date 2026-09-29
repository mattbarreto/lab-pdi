# OpenCV en tres niveles

**Laboratorio de Tecnologías de la Imagen Digital — IFTS24**
Matías Barreto, 2026

Esta unidad organiza el trabajo con OpenCV en tres niveles sucesivos. Cada nivel es una carpeta con sus propios cuadernos, su `README.md` y su `requirements.txt`.

---

## Mapa de la unidad

| Nivel | Carpeta | Pregunta que organiza el nivel | Estado |
|---|---|---|---|
| 1. Introducción | `001_intro/` | ¿Cómo se lee, se describe, se guarda y se encuadra una imagen en OpenCV? | Disponible |
| 2. Fundamental | `002_fundamental/` | ¿Cómo se mejora, se limpia y se segmenta una imagen, y cómo se mide lo segmentado? | En preparación |
| 3. Avanzado | `003_avanzado/` | ¿Cómo se encuentra algo en una imagen, se relacionan dos imágenes y se procesa el video? | En preparación |

### Nivel 1 — Introducción

| Cuaderno | Tema |
|---|---|
| `001_traduccion` | De scikit-image a OpenCV: lectura, BGR y banderas |
| `002_canales` | RGB, escala de grises y HSV |
| `003_archivos` | Formatos, compresión y pérdida |
| `004_encuadre` | Recorte, redimensionado, interpolación y espejado |
| `005_resolucion` | Muestreo y cuantización |
| `006_anotacion` | Dibujar y escribir sobre la imagen |
| `007_ficha` | Integrador: ficha técnica de una imagen propia y script |

El detalle de los niveles 2 y 3 está en el `README.md` de cada carpeta.

---

## Estructura

```
003_opencv/
├── imagenes/          ← imágenes compartidas por los tres niveles
├── 001_intro/
├── 002_fundamental/
└── 003_avanzado/
```

Los cuadernos leen las imágenes desde `../imagenes`. Si descargan un solo nivel, descarguen también la carpeta `imagenes` y ubíquenla junto a la carpeta del nivel.

---

## Entorno

Todos los niveles usan **Python 3.12** y [uv](https://docs.astral.sh/uv/). Las instrucciones de instalación están en el `README.md` de cada nivel.

**Versión de OpenCV.** Los `requirements.txt` fijan `opencv-python>=4.10,<5`. OpenCV 5.0 quitó `cv2.CascadeClassifier` de los bindings de Python, una clase que se usa en la detección clásica de rostros. El nivel avanzado va a revisar esa decisión cuando incorpore detectores basados en redes neuronales.
